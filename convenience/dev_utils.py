def time_func(func, print_elapsed=True):
    import time
    ip = time.process_time()
    func_result = func()
    elapsed = time.process_time() - ip
    if print_elapsed:
        print(elapsed)
        return func_result

    return func_result, elapsed

def get_object_methods(obj):
    return [method_name for method_name in dir(obj) if method_name[:2] != "__" and callable(getattr(obj))]
