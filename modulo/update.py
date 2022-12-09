import AutoUpdate

AutoUpdate.set_url('https://raw.githubusercontent.com/Sidehenrique/CCIS/master/versao.txt')
AutoUpdate.set_current_version("0.0.1")


print(AutoUpdate.is_up_to_date())


