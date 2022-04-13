from app import (flaskapp,shutdown_Mp, videoReaderDict,
                signal_handler, exit_system_local)

if __name__ == "__main__":
    try:
        flaskapp.run(debug = flaskapp.config['DEBUG'], port=5000)
        print("complete")
    except KeyboardInterrupt:
        print("The keyboard Interruption shut down has begun")
        exit_system_local()
        print("Shutting down completed")
    #finally:
    #    exit_system_local()