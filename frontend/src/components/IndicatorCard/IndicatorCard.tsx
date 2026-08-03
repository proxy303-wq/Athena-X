type Props = {

    ema20: number;

    ema50: number;

    rsi: number;

    vwap: number;

    priceAboveEMA20: boolean;

    ema20AboveEMA50: boolean;

    priceAboveVWAP: boolean;

};

export default function IndicatorCard({

    ema20,

    ema50,

    rsi,

    vwap,

    priceAboveEMA20,

    ema20AboveEMA50,

    priceAboveVWAP,

}: Props) {

    const rowStyle = {

        display: "flex",

        justifyContent: "space-between",

        alignItems: "center",

        marginBottom: "18px",

    };

    const badge = (good: boolean) => (

        <span

            style={{

                color: good ? "#22c55e" : "#ef4444",

                fontWeight: 700,

            }}

        >

            {good ? "▲" : "▼"}

        </span>

    );

    return (

        <div

            style={{

                background: "#1e293b",

                borderRadius: 18,

                padding: 28,

                boxShadow: "0 0 25px rgba(0,0,0,.25)",

            }}

        >

            <h2

                style={{

                    marginBottom: 24,

                    fontSize: 24,

                }}

            >

                Indicators

            </h2>

            <div style={rowStyle}>

                <span>EMA 20</span>

                <strong>{ema20.toFixed(2)}</strong>

                {badge(priceAboveEMA20)}

            </div>

            <div style={rowStyle}>

                <span>EMA 50</span>

                <strong>{ema50.toFixed(2)}</strong>

                {badge(ema20AboveEMA50)}

            </div>

            <div style={rowStyle}>

                <span>RSI</span>

                <strong>{rsi.toFixed(2)}</strong>

                <span

                    style={{

                        color:

                            rsi > 70

                                ? "#ef4444"

                                : rsi < 30

                                ? "#22c55e"

                                : "#facc15",

                        fontWeight: 700,

                    }}

                >

                    {rsi > 70
                        ? "OVERBOUGHT"
                        : rsi < 30
                        ? "OVERSOLD"
                        : "NEUTRAL"}

                </span>

            </div>

            <div style={rowStyle}>

                <span>VWAP</span>

                <strong>{vwap.toFixed(2)}</strong>

                {badge(priceAboveVWAP)}

            </div>

        </div>

    );

}