from typing import Optional, Text, Tuple, Union

_SndHeaders = Tuple[str, int, int, int, Union[int, str]]

def what(filename: Text) -> Optional[_SndHeaders]: ...
def whathdr(filename: Text) -> Optional[_SndHeaders]: ...