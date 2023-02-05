# 3.
# Write a function is_prime that takes 1 argument - a number from 2 to 1000,
# and returns True if it is a prime number, and False otherwise.


def is_prime(number: int) -> bool:
    """
    Method checks that digit is prime in range (2, 1000)
    :param number: any int (2, 1000)
    :return: bool
    """
    if number < 2 or number > 1000:
        print('The number is out of range, please use 2-1000 numbers')
    # Exception for algorithm
    elif number in [2, 3]:
        return True
    else:
        for num in range(2, number):
            if number % num != 0:
                result = number / num
                result = str(result).split('.')[-1]
                if result != 0:
                    continue
                else:
                    return False
            else:
                return False
        return True


prime_to_1000 = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97', '101', '103', '107', '109', '113', '127', '131', '137', '139', '149', '151', '157', '163', '167', '173', '179', '181', '191', '193', '197', '199', '211', '223', '227', '229', '233', '239', '241', '251', '257', '263', '269', '271', '277', '281', '283', '293', '307', '311', '313', '317', '331', '337', '347', '349', '353', '359', '367', '373', '379', '383', '389', '397', '401', '409', '419', '421', '431', '433', '439', '443', '449', '457', '461', '463', '467', '479', '487', '491', '499', '503', '509', '521', '523', '541', '547', '557', '563', '569', '571', '577', '587', '593', '599', '601', '607', '613', '617', '619', '631', '641', '643', '647', '653', '659', '661', '673', '677', '683', '691', '701', '709', '719', '727', '733', '739', '743', '751', '757', '761', '769', '773', '787', '797', '809', '811', '821', '823', '827', '829', '839', '853', '857', '859', '863', '877', '881', '883', '887', '907', '911', '919', '929', '937', '941', '947', '953', '967', '971', '977', '983', '991', '997', '1009']

if __name__ == '__main__':
    for i in range(2, 1000):
        if is_prime(i):
            assert (str(i) in prime_to_1000), f'{i} exist in prime array'
        else:
            assert (str(i) not in prime_to_1000), f'{i} NOT exist in prime array'
