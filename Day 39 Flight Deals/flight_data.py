class FlightData:

    def __init__(self, flight):
        self.id = flight['id']
        self.flyFrom = flight['flyFrom']
        self.flyTo = flight['flyTo']
        self.cityFrom = flight['cityFrom']
        self.cityCodeFrom = flight['cityCodeFrom']
        self.cityTo = flight['cityTo']
        self.cityCodeTo = flight['cityCodeTo']
        self.countryFrom_code = flight['countryFrom']['code']
        self.countryFrom_name = flight['countryFrom']['name']
        self.countryTo_code = flight['countryTo']['code']
        self.countryTo_name = flight['countryTo']['name']
        self.nightsInDest = flight['nightsInDest']
        self.quality = flight['quality']
        self.distance = flight['distance']
        self.duration_departure = flight['duration']['departure']
        self.duration_return = flight['duration']['return']
        self.duration_total = flight['duration']['total']
        self.price = flight['price']
        self.conversion_EUR = flight['conversion']['EUR']
        self.bags_price_1 = flight['bags_price']['1']
        self.availability_seats = flight['availability']['seats']
        self.routes_outbound_from = flight['routes'][0][0]
        self.routes_outbound_to = flight['routes'][0][1]
        self.routes_inbound_from = flight['routes'][1][0]
        self.routes_inbound_to = flight['routes'][1][1]
        self.airlines = flight['airlines'][0]
        self.route_outbound_id = flight['route'][0]['id']
        self.route_outbound_combination_id = flight['route'][0]['combination_id']
        self.route_outbound_flyFrom = flight['route'][0]['flyFrom']
        self.route_outbound_flyTo = flight['route'][0]['flyTo']
        self.route_outbound_cityFrom = flight['route'][0]['cityFrom']
        self.route_outbound_cityCodeFrom = flight['route'][0]['cityCodeFrom']
        self.route_outbound_cityTo = flight['route'][0]['cityTo']
        self.route_outbound_cityCodeTo = flight['route'][0]['cityCodeTo']
        self.route_outbound_airline = flight['route'][0]['airline']
        self.route_outbound_flight_no = flight['route'][0]['flight_no']
        self.route_outbound_operating_carrier = flight['route'][0]['operating_carrier']
        self.route_outbound_operating_flight_no = flight['route'][0]['operating_flight_no']
        self.route_outbound_fare_basis = flight['route'][0]['fare_basis']
        self.route_outbound_fare_category = flight['route'][0]['fare_category']
        self.route_outbound_fare_classes = flight['route'][0]['fare_classes']
        self.route_outbound_fare_family = flight['route'][0]['fare_family']
        self.route_outbound_return = flight['route'][0]['return']
        self.route_outbound_bags_recheck_required = flight['route'][0]['bags_recheck_required']
        self.route_outbound_vi_connection = flight['route'][0]['vi_connection']
        self.route_outbound_guarantee = flight['route'][0]['guarantee']
        self.route_outbound_last_seen = flight['route'][0]['last_seen']
        self.route_outbound_refresh_timestamp = flight['route'][0]['refresh_timestamp']
        self.route_outbound_equipment = flight['route'][0]['equipment']
        self.route_outbound_vehicle_type = flight['route'][0]['vehicle_type']
        self.route_outbound_local_arrival = flight['route'][0]['local_arrival'].split('T')[0]
        self.route_outbound_utc_arrival = flight['route'][0]['utc_arrival'].split('T')[0]
        self.route_outbound_local_departure = flight['route'][0]['local_departure'].split('T')[0]
        self.route_outbound_utc_departure = flight['route'][0]['utc_departure'].split('T')[0]
        self.route_inbound_id = flight['route'][1]['id']
        self.route_inbound_combination_id = flight['route'][1]['combination_id']
        self.route_inbound_flyFrom = flight['route'][1]['flyFrom']
        self.route_inbound_flyTo = flight['route'][1]['flyTo']
        self.route_inbound_cityFrom = flight['route'][1]['cityFrom']
        self.route_inbound_cityCodeFrom = flight['route'][1]['cityCodeFrom']
        self.route_inbound_cityTo = flight['route'][1]['cityTo']
        self.route_inbound_cityCodeTo = flight['route'][1]['cityCodeTo']
        self.route_inbound_airline = flight['route'][1]['airline']
        self.route_inbound_flight_no = flight['route'][1]['flight_no']
        self.route_inbound_operating_carrier = flight['route'][1]['operating_carrier']
        self.route_inbound_operating_flight_no = flight['route'][1]['operating_flight_no']
        self.route_inbound_fare_basis = flight['route'][1]['fare_basis']
        self.route_inbound_fare_category = flight['route'][1]['fare_category']
        self.route_inbound_fare_classes = flight['route'][1]['fare_classes']
        self.route_inbound_fare_family = flight['route'][1]['fare_family']
        self.route_inbound_return = flight['route'][1]['return']
        self.route_inbound_bags_recheck_required = flight['route'][1]['bags_recheck_required']
        self.route_inbound_vi_connection = flight['route'][1]['vi_connection']
        self.route_inbound_guarantee = flight['route'][1]['guarantee']
        self.route_inbound_last_seen = flight['route'][1]['last_seen']
        self.route_inbound_refresh_timestamp = flight['route'][1]['refresh_timestamp']
        self.route_inbound_equipment = flight['route'][1]['equipment']
        self.route_inbound_vehicle_type = flight['route'][1]['vehicle_type']
        self.route_inbound_local_arrival = flight['route'][1]['local_arrival'].split('T')[0]
        self.route_inbound_utc_arrival = flight['route'][1]['utc_arrival'].split('T')[0]
        self.route_inbound_local_departure = flight['route'][1]['local_departure'].split('T')[0]
        self.route_inbound_utc_departure = flight['route'][1]['utc_departure'].split('T')[0]
        self.booking_token = flight['booking_token']
        self.deep_link = flight['deep_link']
        self.tracking_pixel = flight['tracking_pixel']
        self.facilitated_booking_available = flight['facilitated_booking_available']
        self.pnr_count = flight['pnr_count']
        self.has_airport_change = flight['has_airport_change']
        self.technical_stops = flight['technical_stops']
        self.throw_away_ticketing = flight['throw_away_ticketing']
        self.hidden_city_ticketing = flight['hidden_city_ticketing']
        self.virtual_interlining = flight['virtual_interlining']
        self.local_arrival = flight['local_arrival'].split('T')[0]
        self.utc_arrival = flight['utc_arrival'].split('T')[0]
        self.local_departure = flight['local_departure'].split('T')[0]
        self.utc_departure = flight['utc_departure'].split('T')[0]
