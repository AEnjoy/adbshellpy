#!/system/bin/sh
touch /sdcard/Android/everythingcompile3rd.sh
echo "$(pm list package -3)"> /sdcard/Android/everythingcompile3rd.sh
sed -i 's/package:/cmd package compile -m everything /g' /sdcard/Android/everythingcompile3rd.sh
sh /sdcard/Android/everythingcompile3rd.sh
rm /sdcard/Android/everythingcompile3rd.sh