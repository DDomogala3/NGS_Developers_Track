"""
patholib_v0.py

Objective:
A simple command-line concierge to help pathologists and clinicians (with limited coding background)
select and use Python or R libraries for data analysis and machine learning.
"""

class PathoLibConcierge:
    """
    The PathoLibConcierge guides the user in selecting and using relevant data science or ML libraries.
    """
    datascience_libs = ["pandas", "polars", "matplotlib", "numpy"]
    ml_libs = ["pytorch", "tensorflow"]
    r_packages = ["maftools", "fishplot"]

    def __init__(self):
        self.selected_libs = []

    def greet(self):
        print("Hello, welcome to PathoLib!")
        print("I am your concierge. I can assist you in selecting, installing, and using data science libraries.")
        print("Let's get started.\n")

    def ask_project_info(self):
        project = input("What type of project are you working on? (e.g., survival analysis, plotting mutations): ")
        print("Great! For '{}', here are some libraries that may help:".format(project))
        print("Python data science: ", ", ".join(self.datascience_libs))
        print("Python ML: ", ", ".join(self.ml_libs))
        print("R packages: ", ", ".join(self.r_packages))
        return project

    def ask_libraries(self):
        libs = input("Which libraries would you like to use? (separate by comma): ")
        self.selected_libs = [lib.strip() for lib in libs.split(",") if lib.strip()]
        print("You selected: {}".format(", ".join(self.selected_libs)))

    def show_install_instructions(self):
        print("\nInstallation instructions:")
        for lib in self.selected_libs:
            if lib in self.datascience_libs or lib in self.ml_libs:
                print(f"- For Python '{lib}': pip install {lib}")
            elif lib in self.r_packages:
                print(f"- For R '{lib}': install.packages('{lib}') (or Bioconductor if needed)")
            else:
                print(f"- Library '{lib}': Not recognized, please check spelling or consult documentation.")

    def run(self):
        self.greet()
        self.ask_project_info()
        self.ask_libraries()
        self.show_install_instructions()

if __name__ == "__main__":
    concierge = PathoLibConcierge()
    concierge.run()