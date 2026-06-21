from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from musubi_tuner.gui_dashboard.metrics_writer import MetricsWriter


def create_metrics_writer(run_dir: str, flush_every: int = 2, reset: bool = False) -> "MetricsWriter":
    from musubi_tuner.gui_dashboard.metrics_writer import MetricsWriter

    return MetricsWriter(run_dir, flush_every=flush_every, reset=reset)


def start_gui_server(run_dir: str, host: str = "0.0.0.0", port: int = 7860):
    from musubi_tuner.gui_dashboard.server import start_server

    return start_server(run_dir, host=host, port=port)
