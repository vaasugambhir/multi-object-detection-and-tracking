from typing import Optional


from ocsort.ocsort import OCSort


from trackerhub.utils.config_utils import get_config

DEFAULT_BYTETRACK_CONFIG_PATH = "trackerhub/configs/byte_track.yaml"
DEFAULT_OCSORT_CONFIG_PATH = "trackerhub/configs/oc_sort.yaml"
DEFAULT_NORFAIR_CONFIG_PATH = "trackerhub/configs/norfair_track.yaml"
DEFAULT_SORT_CONFIG_PATH = "trackerhub/configs/sort_track.yaml"


def create_tracker(
    tracker_type,
    tracker_config_path,
    conf_th: Optional[str] = 0.05,
    iou_th: Optional[str] = 0.05,
) -> object:
    if tracker_type == "OC_SORT":
        if tracker_config_path is None:
            config_path = DEFAULT_OCSORT_CONFIG_PATH
        else:
            config_path = tracker_config_path

        config = get_config(config_path)
        oc_sort = OCSort(
            det_thresh=conf_th,
            max_age=config.OC_SORT.MAX_AGE,
            min_hits=config.OC_SORT.MIN_HITS,
            iou_threshold=iou_th,
            delta_t=config.OC_SORT.DELTA_T,
            asso_func=config.OC_SORT.ASSO_FUNC,
            inertia=config.OC_SORT.INERTIA,
            use_byte=config.OC_SORT.USE_BYTE,
        )
        return oc_sort

    else:
        raise ValueError(f"No such tracker: {tracker_type}")
