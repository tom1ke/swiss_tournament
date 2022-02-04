from controllers.controller import Controller


def main():
    """
    Instancie un contrôleur
    Appelle la méthode Controller.run pour lancer le programme
    """
    controller = Controller()

    controller.run()


if __name__ == "__main__":
    main()
