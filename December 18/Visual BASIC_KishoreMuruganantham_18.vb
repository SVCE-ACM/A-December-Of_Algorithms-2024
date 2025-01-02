Function gem_value(gem As Char) As Integer
    Select Case gem
        Case "D"c
            Return 500
        Case "R"c
            Return 250
        Case "E"c
            Return 100
        Case Else
            Return 0
    End Select
End Function

Function max_palindromic_chain_profit(chain As String) As Integer
    Dim n As Integer = chain.Length
    If n = 0 Then
        Return 0
    End If

    Dim s As String = "@#" & String.Join("#", chain.ToCharArray()) & "#$"
    Dim p(s.Length - 1) As Integer
    Dim c As Integer = 0
    Dim r As Integer = 0

    For i As Integer = 1 To s.Length - 2
        If i < r Then
            p(i) = Math.Min(r - i, p(2 * c - i))
        End If
        While s(i + p(i) + 1) = s(i - p(i) - 1)
            p(i) += 1
        End While
        If i + p(i) > r Then
            c = i
            r = i + p(i)
        End If
    Next

    Dim max_length As Integer = 0
    Dim center As Integer = 0
    For i As Integer = 1 To s.Length - 2
        If p(i) > max_length Then
            max_length = p(i)
            center = i
        End If
    Next

    Dim start As Integer = (center - max_length) \ 2
    Dim [end] As Integer = (center + max_length) \ 2

    Dim total_value As Integer = 0
    For i As Integer = start To [end]
        total_value += gem_value(chain(i))
    Next

    Dim profit As Integer = total_value * ([end] - start + 1)
    Return profit
End Function
