#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: Conan is supported on a best-effort basis. Abseil doesn't use Conan
# internally, so we won't know if it stops working. We may ask community
# members to help us debug any problems that arise.

import os
from conans import ConanFile, CMake, tools


class AbseilConan(ConanFile):
    name = "abseil"
    version = "20210618"
    url = "https://github.com/abseil/abseil-cpp"
    homepage = url
    author = "Abseil <abseil-io@googlegroups.com>"
    description = "Abseil Common Libraries (C++) from Google"
    license = "Apache-2.0"
    topics = ("conan", "abseil", "abseil-cpp", "google", "common-libraries")
    exports = ["LICENSE"]
    exports_sources = ["CMakeLists.txt", "CMake/*", "absl/*"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"

    _cmake = None

    def configure(self):
        if self.settings.compiler.cppstd:
            tools.check_min_cppstd(self, 11)

    def _configure_cmake(self):
        if self._cmake:
            return self._cmake
        tools.replace_in_file(
            "CMakeLists.txt", 
            "project(absl LANGUAGES CXX)", 
            f"project(absl LANGUAGES CXX VERSION {self.version})"
        )
        self._cmake = CMake(self)
        self._cmake.definitions["CMAKE_CXX_STANDARD"] = self.settings.compiler.cppstd
        self._cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = True
        self._cmake.definitions["BUILD_TESTING"] = False
        self._cmake.configure()
        return self._cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy("LICENSE", dst="licenses", src=self.source_folder)
        cmake = self._configure_cmake()
        cmake.install()
        tools.rmdir(os.path.join(self.package_folder, "lib", "pkgconfig"))

    def package_info(self):
        self.cpp_info.includedirs = []
        self.cpp_info.libs = []
        self.user_info.version = self.version
