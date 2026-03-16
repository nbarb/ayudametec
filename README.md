# Ayudame - Remote Desktop by JMV Sistemas

Ayudame is a remote desktop application that allows you to securely access and control remote computers. Built with Rust and Flutter for performance and cross-platform support.

## Build

### Prerequisites

- Rust toolchain (1.75+)
- vcpkg with dependencies: `libvpx`, `libyuv`, `opus`, `aom`
- Set `VCPKG_ROOT` environment variable

### Linux Dependencies

**Ubuntu / Debian:**

```sh
sudo apt install -y zip g++ gcc git curl wget nasm yasm libgtk-3-dev clang libxcb-randr0-dev libxdo-dev \
        libxfixes-dev libxcb-shape0-dev libxcb-xfixes0-dev libasound2-dev libpulse-dev cmake make \
        libclang-dev ninja-build libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libpam0g-dev
```

### Build Commands

```sh
# Native (Sciter UI)
cargo build --release

# Flutter UI
python3 build.py --flutter
```

## License

AGPL-3.0

---

Based on [RustDesk](https://github.com/rustdesk/rustdesk)
