a, b = input().split(".")

la = ["dib", "doc", "docx", "htm", "html", "hwp", "hwpx", "hwt", "jpe", "jpeg", "jpg", "ppt", "pptx", "pptxml"]
lb = ["Paint.Picture", "Word.Document.8", "Word.Document.12", "htmfile", "htmlfile", "Hwp.Document.96", "Hwp.Document.hwpx.96", "Hwp.Document.hwt.96", "jpegfile", "PowerPoint.Show.8", "PowerPoint.Show.12", "powerpointxmlfile"]

for i in range(0, len(la)) :
    if b == la[i] :
        if i == 8 or i == 9 or i == 10 :
            print(lb[8])
        elif i > 10 :
            print(lb[i-2])
        else :
            print(lb[i])

