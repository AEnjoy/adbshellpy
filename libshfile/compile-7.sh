#!/system/bin/sh
touch /sdcard/Android/speedcompile3rd.sh
echo "$(pm list package -3)"> /sdcard/Android/speedcompile3rd.sh
sed -i 's/package:/cmd package compile -m speed -f /g' /sdcard/Android/speedcompile3rd.sh
sh /sdcard/Android/speedcompile3rd.sh
rm /sdcard/Android/speedcompile3rd.sh