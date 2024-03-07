def return_wage(parcel_delivered: int):
    return __check_successful_delivery(parcel_delivered) + 5_000


def __check_successful_delivery(parcel_delivered: int):
    if 0 < parcel_delivered < 50:
        return __calculate_deliveries_less_than_50(parcel_delivered)
    elif 50 <= parcel_delivered < 60:
        return __calculate_deliveries_less_than_sixty_percent(parcel_delivered)
    elif 60 <= parcel_delivered < 70:
        return __calculate_deliveries_less_than_seventy_percent(parcel_delivered)
    elif 70 <= parcel_delivered <= 100:
        return __calculate_deliveries_greater_than_seventy_percent(parcel_delivered)
    else:
        raise RuntimeError("Incorrect percentage")


def __calculate_deliveries_greater_than_seventy_percent(parcel_delivered: int):
    return parcel_delivered * 500


def __calculate_deliveries_less_than_seventy_percent(parcel_delivered):
    return parcel_delivered * 250


def __calculate_deliveries_less_than_sixty_percent(parcel_delivered):
    return parcel_delivered * 200


def __calculate_deliveries_less_than_50(parcel_delivered):
    return parcel_delivered * 160


