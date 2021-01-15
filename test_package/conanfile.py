from conans import ConanFile, CMake
import pathlib


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        bin_path = pathlib.Path("bin", "test_package")
        self.run(f"{bin_path} -s", run_environment=True)
