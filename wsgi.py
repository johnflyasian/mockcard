from app import (flaskapp)

if __name__ == "__main__":
    try:
        flaskapp.run(debug = False, port=5000)
        print("complete")
    except KeyboardInterrupt:
        pass
    #finally:
    #    exit_system_local()