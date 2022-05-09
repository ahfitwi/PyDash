def def_ver():
    df_ver1 = pd.DataFrame({'System Attribute': ['Date', 'User Name', 'System', 
                       'Node', 'Release','Version', 'Machine', 'Processor', 
                       'Python Version', '# of CPU Cores'], 
                       'Description':[dtt.now().strftime("%Y-%B-%d %H:%M:%S"),
                        platform.uname(), platform.system(),
                        platform.node(),platform.release(), platform.version(),
                        platform.machine(), platform.processor(),
                        platform.python_version(), 
                        multiprocessing.cpu_count()]
                       })
    return df_ver1