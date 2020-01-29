from python_workflow import steps


class All:
    def __init__(self):
        """
        Set the order of your steps here.
        """
        self.step_list = [steps.Raw()]

    def run(self):
        """
        Run all steps.
        """
        for step in self.step_list:
            step.run()

    def pull(self):
        """
        Pull all steps.
        """
        for step in self.step_list:
            step.pull()

    def checkout(self):
        """
        Checkout all steps.
        """
        for step in self.step_list:
            step.checkout()

    def push(self):
        """
        Push all steps.
        """
        for step in self.step_list:
            step.push()
