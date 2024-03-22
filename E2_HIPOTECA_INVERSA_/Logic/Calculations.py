import Exceptions as E

"""
Parameters:
    total_amount : Total price of the house or dwelling
    interest : This is the interest that will be applied to the loan
    quotas : If requested, this is the number of installments at which the Loan will be made
    interest_housing: It is the interest that will be applied to the normal price of the house
"""

def MortgageLifetimeInverse(total_amount, interest, quotas, interest_housing):

    """
        Definition:
            Lifetime reverse mortgage: the client collects the annuity until he or she dies. The function returns the calculation

        Returns:
            float: The amount of money to be received periodically in a lifetime reverse mortgage.
    """

    if total_amount < 0 or interest < 0 or quotas < 0:
        raise E.invalid_valor()
    EvaluatePropertyValueCalculation(total_amount)
    InterestCalculation(interest)
    if quotas == 0:
        raise E.invalid_quotas()    

    return total_amount / (quotas * interest_housing)

def MortgageTemporaryReverse(total_amount, interest, quotas, interest_housing):

    """
        Definition:
            Temporary reverse mortgage: the rent is obtained for a set period of time.
        Returns:
            float: The total amount of money to be received during the established installment period.
    """

    if total_amount < 0 or interest < 0 or quotas < 0:
        raise E.invalid_valor()
    EvaluatePropertyValueCalculation(total_amount)
    InterestCalculation(interest)
    if quotas == 0:
        raise E.invalid_quotas()    

    return total_amount / (quotas * interest_housing)

def MortgageSingleReverse(total_amount, interest, quotas, interest_housing):

    """
        Definition:
            Single-draw reverse mortgage: The value to be received will be the total sale value of the home.
        Returns:
            float: The total value of the home.
    """

    if total_amount < 0 or interest < 0 or quotas < 0:
        raise E.invalid_valor()
    EvaluatePropertyValueCalculation(total_amount)
    InterestCalculation(interest)
    if quotas == 0:
        raise E.invalid_quotas()    

    return total_amount / (quotas * interest_housing)

def LifeExpectancyCalculation(age, gender):
    "Retorna el calculo de la esperanza de vida en base al genero y la edad"
    if age < 65:
        raise E.invalid_age()
    if gender == "M":
        return 74 - age
    if gender == "F":
        return 81 - age
    
def InterestCalculation(interest):
    "Evalua si el interes anual es alto"
    if interest <= 0:
        raise E.invalid_interest()
    if interest > 0.007974:
        raise E.hight_interest()
    else:
        return True
    return

def EvaluatePropertyValueCalculation(total_amount):
    "Evalua si el valor de la propiedad es muy alto, muy bajo o está bien en Colombia"
    if total_amount < 52000000:
        raise E.low_amount_property()
    return