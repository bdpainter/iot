# Shadow devices mirror physical devices, but with an always-on
# service. The real devices may sleep or be unavailable.
#


class Shadow(object):
    def __init__(self, device_type, device_id):
        """
        The base class for device shadows. This should not be instantiated directly.

        * device_type:  The type of the device, e.g. "candle". Must be the
                        same as the device type in corresponding MQTT messages
        * device_id:    An ID, unique for each device type. E.g. "0", "1", etc.
        """
        self._device_type = device_type
        self._device_id = device_id        # Unique ID for this instance of this device