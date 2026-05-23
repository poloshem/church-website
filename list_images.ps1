$root = "C:\Users\Ruknalabeer.com\Desktop\CHURCH WEBSITE"
$exts = @(".jpg",".jpeg",".png",".gif",".webp",".bmp",".tiff")
Get-ChildItem -Path $root -Directory -Recurse -Force | Where-Object { $_.Name -ieq "images" } | ForEach-Object {
  Get-ChildItem -Path $_.FullName -File -Force | Where-Object { $exts -contains $_.Extension.ToLower() }
} | Sort-Object LastWriteTime -Descending | Select-Object -First 20 FullName, LastWriteTime