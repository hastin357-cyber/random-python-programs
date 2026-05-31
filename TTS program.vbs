Set sapi = CreateObject("SAPI.SpVoice")
Dim ans, idk
idk = True
Do While True
ans = InputBox("put what you want in here", "TTS BOX", , -15000, 500)
If ans = "/stop" Then
    Exit Do
    idk = False
End If
sapi.Speak ans
Loop