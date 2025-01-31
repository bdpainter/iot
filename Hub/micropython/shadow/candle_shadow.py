from .shadow import Shadow

DEVICE_TYPE = "candle"

class CandleState(object):
    def __init__(self, is_on=False):
        self._is_on = is_on


class CandleShadow(Shadow):
    def __init__(self, device_id):
        super(CandleShadow, self).__init__(device_type=DEVICE_TYPE, device_id=device_id)
        
        self._state_desired = CandleState()
        self._state_reported = CandleState()