EXT=rpm
for i in *; do
    if [ "${i}" != "${i%.${EXT}}" ];then
        echo "extracting $i"
	rpm2cpio $i |cpio -idmv
    fi
done
