Name:       ayudame
Version:    1.0.0
Release:    0
Summary:    RPM package
License:    GPL-3.0
URL:        https://jmvsistemas.com
Vendor:     JMV Sistemas <info@jmvsistemas.com>
Requires:   gtk3 libxcb1 libXfixes3 alsa-utils libXtst6 libva2 pam gstreamer-plugins-base gstreamer-plugin-pipewire
Recommends: libayatana-appindicator3-1 xdotool
Provides:   libdesktop_drop_plugin.so()(64bit), libdesktop_multi_window_plugin.so()(64bit), libfile_selector_linux_plugin.so()(64bit), libflutter_custom_cursor_plugin.so()(64bit), libflutter_linux_gtk.so()(64bit), libscreen_retriever_plugin.so()(64bit), libtray_manager_plugin.so()(64bit), liburl_launcher_linux_plugin.so()(64bit), libwindow_manager_plugin.so()(64bit), libwindow_size_plugin.so()(64bit), libtexture_rgba_renderer_plugin.so()(64bit)

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/

%description
Ayudame Remote Desktop by JMV Sistemas

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

# %global __python %{__python3}

%install

mkdir -p "%{buildroot}/usr/share/ayudame" && cp -r ${HBB}/flutter/build/linux/x64/release/bundle/* -t "%{buildroot}/usr/share/ayudame"
mkdir -p "%{buildroot}/usr/bin"
install -Dm 644 $HBB/res/rustdesk.service -t "%{buildroot}/usr/share/ayudame/files"
install -Dm 644 $HBB/res/rustdesk.desktop -t "%{buildroot}/usr/share/ayudame/files"
install -Dm 644 $HBB/res/rustdesk-link.desktop -t "%{buildroot}/usr/share/ayudame/files"
install -Dm 644 $HBB/res/128x128@2x.png "%{buildroot}/usr/share/icons/hicolor/256x256/apps/ayudame.png"
install -Dm 644 $HBB/res/scalable.svg "%{buildroot}/usr/share/icons/hicolor/scalable/apps/ayudame.svg"

%files
/usr/share/ayudame/*
/usr/share/ayudame/files/ayudame.service
/usr/share/icons/hicolor/256x256/apps/ayudame.png
/usr/share/icons/hicolor/scalable/apps/ayudame.svg
/usr/share/ayudame/files/ayudame.desktop
/usr/share/ayudame/files/ayudame-link.desktop

%changelog
# let's skip this for now

%pre
# can do something for centos7
case "$1" in
  1)
    # for install
  ;;
  2)
    # for upgrade
    systemctl stop ayudame || true
  ;;
esac

%post
cp /usr/share/ayudame/files/ayudame.service /etc/systemd/system/ayudame.service
cp /usr/share/ayudame/files/ayudame.desktop /usr/share/applications/
cp /usr/share/ayudame/files/ayudame-link.desktop /usr/share/applications/
ln -sf /usr/share/ayudame/ayudame /usr/bin/ayudame
systemctl daemon-reload
systemctl enable ayudame
systemctl start ayudame
update-desktop-database

%preun
case "$1" in
  0)
    # for uninstall
    systemctl stop ayudame || true
    systemctl disable ayudame || true
    rm /etc/systemd/system/ayudame.service || true
  ;;
  1)
    # for upgrade
  ;;
esac

%postun
case "$1" in
  0)
    # for uninstall
    rm /usr/bin/ayudame || true
    rmdir /usr/lib/ayudame || true
    rmdir /usr/local/ayudame || true
    rmdir /usr/share/ayudame || true
    rm /usr/share/applications/ayudame.desktop || true
    rm /usr/share/applications/ayudame-link.desktop || true
    update-desktop-database
  ;;
  1)
    # for upgrade
    rmdir /usr/lib/ayudame || true
    rmdir /usr/local/ayudame || true
  ;;
esac
