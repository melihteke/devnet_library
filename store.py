class Store():
    """
    The Store class represents a retail store in the network infrastructure. It includes store-specific information such as the store number, geographical location, and store type.

    The class constructor takes the following parameters:
    - store_number (int): a unique identifier for the store.
    - geo (str): the geographical location of the store. Defaults to 'emea'.
    - store_type (str): the type of store. Defaults to 'nike'.

    The Store class provides a convenient way to store and access store-related data within the retail network infrastructure. By creating an instance of the Store class for each store in the network, developers and network administrators can more easily manage store-specific configurations, policies, and settings. 

    Instances of the Store class can be used in conjunction with other classes and modules to enable efficient and scalable network management for the retail environment.
    """

    def __init__(self, store_number, geo='emea', store_type='nike') -> None:

        self.store_number = store_number
        self.geo = geo
        self.store_type = store_type



