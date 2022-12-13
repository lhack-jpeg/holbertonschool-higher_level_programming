$(document).ready(() => {
    $("#btn_translate").click(() => {
        const langCode = $("#language_code").val();
        console.log({ langCode });
        $.ajax({
            url: `https://stefanbohacek.com/hellosalut/?lang=${langCode}`,
            type: "get",
            success: (data, status) => {
                $("#hello").text(data.hello);
            },
        });
    });
});
