from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    VALID_ARTEFACTS = {"RenaissanceArtifact": RenaissanceArtifact, "ContemporaryArtifact": ContemporaryArtifact}
    VALID_COLLECTORS = {"Museum": Museum, "PrivateCollector": PrivateCollector}

    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []
        self.sold_artifacts: list[BaseArtifact] = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float,
                          artifact_space: int) -> str:
        if artifact_type not in self.VALID_ARTEFACTS.keys():
            raise ValueError("Unknown artifact type!")

        found_artefact = self.search_object(artifact_name, self.artifacts)
        if found_artefact:
            raise ValueError(f"{artifact_name} has been already registered!")

        artefact = self.VALID_ARTEFACTS[artifact_type](artifact_name, artifact_price, artifact_space)
        self.artifacts.append(artefact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self.VALID_COLLECTORS.keys():
            raise ValueError("Unknown collector type!")

        found_collector = self.search_object(collector_name, self.collectors)
        if found_collector:
            raise ValueError(f"{collector_name} has been already registered!")

        collector = self.VALID_COLLECTORS[collector_type](collector_name)
        self.collectors.append(collector)
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str) -> str:
        found_collector = self.search_object(collector_name, self.collectors)
        if not found_collector:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        found_artefact = self.search_object(artifact_name, self.artifacts)
        if not found_artefact:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if not found_collector.can_purchase(found_artefact.price, found_artefact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(found_artefact)
        found_collector.purchased_artifacts.append(found_artefact)
        self.sold_artifacts.append(found_artefact)
        found_collector.available_money -= found_artefact.price
        found_collector.available_space -= found_artefact.space_required

        return f"{collector_name} purchased {artifact_name} for a price of {found_artefact.price:.2f}."

    def remove_artifact(self, artifact_name: str) -> str | None:
        found_artefact = self.search_object(artifact_name, self.artifacts)
        if not found_artefact:
            return "No such artifact."

        if found_artefact and found_artefact not in self.sold_artifacts:
            self.artifacts.remove(found_artefact)
            return f"Removed {found_artefact.artifact_information()}"

    def fundraising_campaigns(self, max_money: float) -> str:
        count = 0
        for collector in self.collectors:
            if collector.available_money <= max_money:
                count += 1
                collector.increase_money()

        return f"{count} collector/s increased their available money."

    def get_auction_report(self) -> str:
        output = [f"**Auction statistics**\n"
                  f"Total number of sold artifacts: {len(self.sold_artifacts)}\n"
                  f"Available artifacts for sale: {len(self.artifacts)}\n"
                  f"***"]

        sorted_collectors = sorted(self.collectors, key=lambda c: (-len(c.purchased_artifacts), c.name))
        for collector in sorted_collectors:
            output.append(str(collector))

        return '\n'.join(output)

    @staticmethod
    def search_object(object_name, collection):
        return next((o for o in collection if o.name == object_name), None)
