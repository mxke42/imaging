import exifread
# Open image file for reading (binary mode)
f = open('Images/test.tiff', 'rb')

# Return Exif tags
tags = exifread.process_file(f)

# Print the tag/ value pairs
print(tags)
# for tag in tags.keys():
#     if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
#         print "Key: %s, value %s" % (tag, tags[tag])