from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter
from multiprocessing import freeze_support
from spleeter.types import AudioDescriptor

separator = Separator("spleeter:2stems")
separator.separate_to_file(filename_format="./akmu.wav", destination="./akmu/")
