"""Constants for the Remootio integration."""

# Domain of the integration
DOMAIN = "remootio"

# Timeout used in methods of remootio.utils
REMOOTIO_TIMEOUT = 60

# Deleay used in methods of remootio.utils
REMOOTIO_DELAY = 0.5

# Expected minimum Remootio Websocket API version supported by this integration
EXPECTED_MINIMUM_API_VERSION = 2

# Keys used by the Config flow
CONF_API_SECRET_KEY = "secret__api_secret_key"
CONF_API_AUTH_KEY = "secret__api_auth_key"
CONF_TITLE = "title"
CONF_SERIAL_NUMBER = "serial_number"
CONF_DATA = "data"

# Keys for event data fired by remootio.cover.RemootioCoverEventListener
ATTR_SERIAL_NUMBER = CONF_SERIAL_NUMBER

# Key for the dictionary entry which holds the instance of aioremootio.RemootioClient to connect to the Remootio device using the Remootio Websocket API
REMOOTIO_CLIENT = "remootio_client"

##
DEFAULT_STATE = "closed"
