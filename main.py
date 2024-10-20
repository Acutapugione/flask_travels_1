from app import app, Config


def main():
    # if app.debug:
    Config.mock_up()

    app.run(debug=True)


if __name__ == "__main__":
    main()
