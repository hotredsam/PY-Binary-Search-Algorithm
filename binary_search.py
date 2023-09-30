# code your iterative algorithm here

def binary_search_recursive(data, el, first, last):
    if first <= last:
        mid = (first + last) // 2

        if data[mid] == el:
            return True
        elif el < data[mid]:
            return binary_search_recursive(data, el, first, mid-1)
        else:
            return binary_search_recursive(data, el, mid+1, last)

    return False

# Test the function
test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]
print(binary_search_recursive(test_list, 11, 0, len(test_list)-1))  # Output should be True
