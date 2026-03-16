Name:       ayudame
Version:    1.0.0
Release:    0
Summary:    RPM package
License:    GPL-3.0
URL:        https://jmvsistemas.com
Vendor:     JMV Sistemas <info@jmvsistemas.com>
Requires:   gtk3 libxcb libXfixes alsa-lib libva2 pam gstreamer1-plugins-base
Recommends: libayatana-appindicator-gtk3 libxdo

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/

%description
Ayudame Remote Desktop by JMV Sistemas

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

%global __python %{__python3}

%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/ayudame/
mkdir -p %{buildroot}/usr/share/ayudame/files/
mkdir -p %{buildroot}/usr/share/icons/hicolor/256x256/apps/
mkdir -p %{buildroot}/usr/share/icons/hicolor/scalable/apps/
install -m 755 $HBB/target/release/rustdesk %{buildroot}/usr/bin/ayudame
install $HBB/libsciter-gtk.so %{buildroot}/usr/share/ayudame/libsciter-gtk.so
install $HBB/res/rustdesk.service %{buildroot}/usr/share/ayudame/files/
install $HBB/res/128x128@2x.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/ayudame.png
install $HBB/res/scalable.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/ayudame.svg
install $HBB/res/rustdesk.desktop %{buildroot}/usr/share/ayudame/files/
install $HBB/res/rustdesk-link.desktop %{buildroot}/usr/share/ayudame/files/

%files
/usr/bin/ayudame
/usr/share/ayudame/libsciter-gtk.so
/usr/share/ayudame/files/ayudame.service
/usr/share/icons/hicolor/256x256/apps/ayudame.png
/usr/share/icons/hicolor/scalable/apps/ayudame.svg
/usr/share/ayudame/files/ayudame.desktop
/usr/share/ayudame/files/ayudame-link.desktop
/usr/share/ayudame/files/__pycache__/*

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
    rm /usr/share/applications/ayudame.desktop || true
    rm /usr/share/applications/ayudame-link.desktop || true
    update-desktop-database
  ;;
  1)
    # for upgrade
  ;;
esac
