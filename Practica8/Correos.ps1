$file = "Contenido-Mail.txt"

if (test-path $file)
{

    $from = "usuario1@empresa.com"
    $to = "usuario2@empresa.com","usuario3@empresa.com"
    #Las direcciones del to deben indicarse con signos de mayor que 
    #y menor que.
    $pc = get-content env:computername
    $subject = "Mesaje de prueba del servidor " + $pc
    $smtpserver = "192.168.1.250"


    #Con Out-String formateamos el texto
    $body = Get-Content $file | Out-String


    foreach ($recipient in $to)
    {
        write-host "Enviando mail a $to"
        Send-MailMessage -smtpServer $smtpserver -from $from -to $recipient -subject $subject  -body $body
    }
}
else
{
write-host "Fichero no encontrado"
}