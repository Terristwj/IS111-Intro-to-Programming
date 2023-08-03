import sys


def run_test():

    print('########## TESTING Q4a ##########')
    # Test Cases
    test_cases = [('flight2.txt' , {'AirAsia': [('Z2825', 'Manila', 'Singapore', 210, 200)], 'Singapore Airlines': [('SQ915', 'Manila', 'Singapore', 230, 177)]},1),
                    ('flight3.txt' , {'Scoot': [('TR427', 'Penang', 'Singapore', 95, 58), ('TR481', 'Ipoh', 'Singapore', 80, 54), ('TR487', 'Ipoh', 'Singapore', 80, 57)], 'Philippine Airlines': [('PR2785', 'Manila', 'Puerto Princesa City', 80, 62)], 'AirAsia': [('AK1311', 'Ipoh', 'Singapore', 75, 57)]},1)]


    # ##########

    total_score = 0.0
    counter = 0
    
    try:
        from q4a import get_flight_durations
        for (filename, expected_result, score) in test_cases:
            print("\nTest Case: get_flight_durations('" + filename + "')")
            try:
                result = get_flight_durations(filename)
                print("Expected output: " , expected_result)
                print("Actual output  : " , result)
                if result == expected_result:
                    total_score += score
                    counter += 1
                    print("+" + str(score) + "/" + str(score) + " marks")
                else:
                    print("+0.0/" + str(score) + " marks")
            except:
                print('Exception:', sys.exc_info())
    except:
        print('Exception:', sys.exc_info())
    
    total_score = round(total_score, 2)
    print('\nTotal Marks: ' + str(total_score) + " out of 2.0")
   
    return (counter, total_score)

if __name__ == "__main__":
    run_test()