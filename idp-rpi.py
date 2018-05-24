from multiprocessing import Process, Pipe

import core.bootstrap as bootstrap
import core.controller as controller

if __name__ == "__main__":
    try:
        interface = bootstrap.bootstrap_interface()
        parent_conn, child_conn = Pipe()
        con_p = Process(target=controller.start, args=(child_conn,))
        con_p.start()
        interface.start(bootstrap.bootstrap_assignments(), parent_conn)
        con_p.join()
    except KeyboardInterrupt:
        print("Exiting..")
        try:
            child_conn.send("exit")
            con_p.join()
        except NameError:
            pass
