def myfunc():

    BookingForms = {
                    "partyName": "tripName",
                    "startDate": "startDate",
                    "salesAgentName": "salesAgentName",
                    "travelAgency": "travelAgency",

                    "tripName": "tripName",
                    "endDate": "endDate",
                    "tourBuilderNumber": "tourBuilderNumber",
                    "travelAgent": "travelAgent",

                    "bookingFormUrl": "bookingFormUrl",

                    "code": "code",
                    "promoNote": "promoNote",

                    "bookingTotal": "bookingTotal",
                    "depositPaymentAmount": "depositPaymentAmount",
                    "finalPaymentAmount": "depositPaymentAmount",

                    "last4Digits": "last4Digits",
                    "paymentMethod": "paymentMethod",
                    "finalPaymentDueDate": "finalPaymentDueDate",

                    "address": "address",
                    "city": "city",
                    "postalCode": "postalCode",
                    "stateOrProvince": "stateOrProvince",
                    "country": "country",
                    
                    "bedPreference": "bedPreference",
                    "roomPreference": "roomPreference",
                    "celebrationPreference": "celebrationPreference",
                    "additionalTravelDetail": "additionalTravelDetail",

                    "number_of_insured_travellers": "otherBedPreference",
                    "cancellation_coverage_amount": "otherBedPreference",
                }
    
    col_names = ['BookingForms', 'TravelAgent', 'Insurance', 'Promotions']
    rows = zip(*[BookingForms[c] for c in col_names])

    return dict(rows=rows, colnames=col_names)
    print(myfunc)


Travellers = {
                    "title": "title",
                    "firstName": "firstName",
                    "middleName": "middleName",
                    "lastName": "lastName",
                    "dateOfBirth": "dateOfBirth",
                    "gender": "gender",
                    "email": "email",
                    "phone": "phone",
                    "phoneWhileTravelling": "phoneWhileTravelling",
                    "emergencyContactPhone": "emergencyContactPhone",
                    "address": "address",
                    "passportNumber": "passportNumber",
                    "passportExpiry": "passportExpiry",
                    "shoeSize": "shoeSize",
                    "weight": "weight",
}


# def create_travellers(data['travellers']):
#     pass