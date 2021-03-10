# Return 0 if system is OK, otherwise a positive integer corresponding to an error code
def check_if_system_is_ok():
  return 0

return_value = check_if_system_is_ok()

if return_value != 0:
  raise Exception("System returned error code " + str(return_value))
