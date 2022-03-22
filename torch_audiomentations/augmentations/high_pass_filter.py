import torch

from ..augmentations.low_pass_filter import LowPassFilter


class HighPassFilter(LowPassFilter):
    """
    Apply high-pass filtering to the input audio.
    """

    supports_multichannel = True
    requires_sample_rate = True

    def __init__(
        self,
        min_cutoff_freq=20,
        max_cutoff_freq=2400,
        mode: str = "per_example",
        p: float = 0.5,
        p_mode: str = None,
        sample_rate: int = None,
        target_rate: int = None,
    ):
        """
        :param min_cutoff_freq: Minimum cutoff frequency in hertz
        :param max_cutoff_freq: Maximum cutoff frequency in hertz
        :param mode:
        :param p:
        :param p_mode:
        :param sample_rate:
        :param target_rate:
        """

        super().__init__(
            min_cutoff_freq,
            max_cutoff_freq,
            mode=mode,
            p=p,
            p_mode=p_mode,
            sample_rate=sample_rate,
            target_rate=target_rate,
        )

    def apply_transform(
        self,
        selected_samples: torch.Tensor,
        sample_rate: int = None,
        targets: torch.Tensor = None,
        target_rate: int = None,
    ):
        low_pass_filtered_samples, low_pass_filtered_targets = super().apply_transform(
            selected_samples.clone(),
            sample_rate,
            targets=targets.clone() if targets is not None else None,
            target_rate=target_rate,
        )
        return selected_samples - low_pass_filtered_samples, low_pass_filtered_targets
