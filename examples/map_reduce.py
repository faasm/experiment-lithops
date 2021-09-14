# Copied from lithops examples:
# https://github.com/lithops-cloud/lithops/blob/master/examples/map_reduce.py
import lithops

iterdata = [1, 2, 3, 4]


def my_map_function(x):
    return x + 7


def my_reduce_function(results):
    total = 0
    for map_result in results:
        total = total + map_result
    return total


if __name__ == "__main__":
    """
    By default the reducer will be launched within a Cloud Function
    when the local Lithops have all the results from the mappers.
    """
    fexec = lithops.FunctionExecutor()
    fexec.map_reduce(my_map_function, iterdata, my_reduce_function)
    print(fexec.get_result())

