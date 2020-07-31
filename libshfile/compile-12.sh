#!/system/bin/sh
touch /sdcard/Android/clear.sh
echo "$(pm list package -3)"> /sdcard/Android/clear.sh
sed -i 's/package:/cmd package compile --reset /g' /sdcard/Android/clear.sh
sh /sdcard/Android/clear.sh
rm /sdcard/Android/clear.sh