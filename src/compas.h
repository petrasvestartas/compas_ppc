// compas.h - Precompiled Header for COMPAS C++ extensions
#pragma once

// Standard library includes
#include <iostream>
#include <vector>
#include <memory>
#include <string>
#include <stdexcept>

// Eigen includes
#include <Eigen/Core>
#include <Eigen/Dense>

// Nanobind includes
#include <nanobind/nanobind.h>
#include <nanobind/stl/vector.h>
#include <nanobind/ndarray.h>
#include <nanobind/eigen/dense.h>
#include <nanobind/stl/string.h>

// Namespace definitions
namespace nb = nanobind;
using namespace nb::literals;
