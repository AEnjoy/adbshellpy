#!/system/bin/sh
touch /sdcard/Android/clearcompile3rd.sh
echo "$(pm list package -3)"> /sdcard/Android/clearcompile3rd.sh
sed -i 's/package:/cmd package compile -m quicken -f /g' /sdcard/Android/clearcompile3rd.sh
sh /sdcard/Android/clearcompile3rd.sh
rm /sdcard/Android/clearcompile3rd.sh