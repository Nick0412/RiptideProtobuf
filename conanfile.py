from conans import ConanFile, tools, CMake
from conan.tools.cmake import CMakeToolchain
import os

class RiptideProtobufConan(ConanFile):
    name = "RiptideProtobuf"
    version = "0.1"
    folder_location = "protobuf"

    def source(self):
        tar_name = "protobuf-cpp-3.21.3.tar.gz"
        tools.download(
            "https://github.com/protocolbuffers/protobuf/releases/download/v21.3/protobuf-cpp-3.21.3.tar.gz",
            tar_name)
        tools.untargz(tar_name, strip_root=True, destination=self.folder_location)
        os.unlink(tar_name)
        
    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        
    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.folder_location)
        cmake.build()
        
    def package(self):
        self.copy("*.h", dst="include", src="protobuf/src")
        self.copy("*.a", dst="lib", keep_path=False)
        
    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.libs = ["protobuf"]