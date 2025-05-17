# Solution

## Dependencies
* zsteg (webshell available)

This image is using LSB, or Least Significant Bit steganography. Try running `zsteg red.png`

As you can see from the output, zsteg will attempt to decode the image using a
number of different steganography techniques. The output of the
`b1,rgba,lsb,xy` technique looks suspiciously like a base64 encoded string, and
when decoded it gives us 4 copies of the flag.
