Imports System.Text.RegularExpressions

Public Class Form1

    Shared random As New Random()

    Private Sub wait(ByVal interval As Integer)
        Dim sw As New Stopwatch
        sw.Start()
        Do While sw.ElapsedMilliseconds < interval
            Application.DoEvents()
        Loop
        sw.Stop()
    End Sub

    Dim array As New Collection
    Dim delay As Integer
    Dim exitAll As Boolean = False

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        array.Add(TextBox1)
        array.Add(TextBox2)
        array.Add(TextBox3)
        array.Add(TextBox4)
        array.Add(TextBox5)
        array.Add(TextBox6)
        array.Add(TextBox7)
        array.Add(TextBox8)
        array.Add(TextBox9)
        array.Add(TextBox10)
        delay = Val(TextBox11.Text)
    End Sub
    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click
        For Each i In array
            i.text = random.Next(0, 100)
        Next
    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        delay = Val(TextBox11.Text)
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        exitAll = False
        Dim num As New Regex("[0-9]")

        For Each box In array
            If box.text = "" Then
                ErrorProvider1.SetError(Button1, "You cant leave the boxes empty!")
                Exit Sub
            End If
        Next

        For Each box In array
            If Not num.IsMatch(box.text) Then
                ErrorProvider1.SetError(Button1, "You cant enter charector! please enter number only")
                Exit Sub
            End If
        Next

        Select Case ComboBox1.SelectedItem
            Case "Bubble sort"
                BubbleSort()
            Case "Selection sort"
                SelectionSort()
            Case "Insertion sort"
                InsertionSort()
        End Select

    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        exitAll = True
        For Each box In array
            box.Text = ""
        Next
    End Sub

    Sub BubbleSort()
        For i = 1 To array.Count
            For j = 1 To array.Count - i
                array(j).BackColor = Color.Red
                array(j + 1).BackColor = Color.Pink
                Label3.Text = array(j).Text + " > " + array(j + 1).Text + " = " + (Val(array(j).Text) > Val(array(j + 1).Text)).ToString
                If exitAll Then
                    array(j).BackColor = Color.White
                    array(j + 1).BackColor = Color.White
                    Button2.PerformClick()
                    Label3.Text = ""
                    Exit Sub
                Else
                    wait(delay)
                End If
                If Val(array(j).Text) > Val(array(j + 1).Text) Then
                    Dim temp As String = array(j).Text
                    array(j).Text = array(j + 1).Text
                    array(j + 1).Text = temp
                End If
                array(j).BackColor = Color.White
                array(j + 1).BackColor = Color.White
            Next
        Next
        Label3.Text = ""
    End Sub

    Sub SelectionSort()
        Dim minIndex As Short
        For i = 1 To array.Count
            minIndex = i
            For j = i + 1 To array.Count
                array(minIndex).BackColor = Color.Red
                array(j).BackColor = Color.Pink
                If Val(array(j).Text) < Val(array(minIndex).Text) Then
                    array(minIndex).BackColor = Color.White
                    minIndex = j
                    array(minIndex).BackColor = Color.Red
                    wait(delay)
                End If
            Next
        Next
    End Sub

    Sub InsertionSort()
        For i = 2 To array.Count
            Dim j As Integer = i
            While j > 1
                If Val(array(j - 1).Text) > Val(array(j).Text) Then
                    Dim temp As String = array(j).Text
                    array(j).BackColor = Color.Red
                    array(j - 1).BackColor = Color.Pink
                    Label3.Text = array(j - 1).Text + " > " + array(j).Text + " = " + (Val(array(j - 1).Text) > Val(array(j).Text)).ToString
                    If exitAll Then
                        array(j).BackColor = Color.White
                        array(j + 1).BackColor = Color.White
                        Button2.PerformClick()
                        Label3.Text = ""
                        Exit Sub
                    Else
                        wait(delay)
                    End If
                    array(j).Text = array(j - 1).Text
                    array(j - 1).Text = temp
                    array(j).BackColor = Color.White
                    array(j - 1).BackColor = Color.White
                End If
                j -= 1
            End While
        Next
        Label3.Text = ""
    End Sub


    'This is just to improve the user experience
    Private Sub TextBox1_TextChanged(sender As Object, e As EventArgs) Handles TextBox1.TextChanged
        ErrorProvider1.Clear()
    End Sub

    Private Sub TextBox2_TextChanged(sender As Object, e As EventArgs) Handles TextBox2.TextChanged
        ErrorProvider1.Clear()
    End Sub

    Private Sub TextBox3_TextChanged(sender As Object, e As EventArgs) Handles TextBox3.TextChanged
        ErrorProvider1.Clear()
    End Sub

    Private Sub TextBox4_TextChanged(sender As Object, e As EventArgs) Handles TextBox4.TextChanged
        ErrorProvider1.Clear()
    End Sub

    Private Sub TextBox5_TextChanged(sender As Object, e As EventArgs) Handles TextBox5.TextChanged
        ErrorProvider1.Clear()
    End Sub

    Private Sub TextBox6_TextChanged(sender As Object, e As EventArgs) Handles TextBox6.TextChanged
        ErrorProvider1.Clear()
    End Sub

    Private Sub TextBox7_TextChanged(sender As Object, e As EventArgs) Handles TextBox7.TextChanged
        ErrorProvider1.Clear()
    End Sub

    Private Sub TextBox8_TextChanged(sender As Object, e As EventArgs) Handles TextBox8.TextChanged
        ErrorProvider1.Clear()
    End Sub

    Private Sub TextBox9_TextChanged(sender As Object, e As EventArgs) Handles TextBox9.TextChanged
        ErrorProvider1.Clear()
    End Sub

    Private Sub TextBox10_TextChanged(sender As Object, e As EventArgs) Handles TextBox10.TextChanged
        ErrorProvider1.Clear()
    End Sub

End Class
