
a=$(./randall 8 | wc -c); if [ $a -eq 8 ]; then echo "success"; else echo "fail"; fi
b=$(./randall -o std 200 | wc -c); if [$b -eq 200]; then echo "success"; else echo "fail"; fi
c=$(./randall -i rdrand 50 | wc -c); if [$c -eq 50]; then echo "success"; else echo "fail"; fi
