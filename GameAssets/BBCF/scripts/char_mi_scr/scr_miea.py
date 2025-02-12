@Subroutine
def Funnel_Pallet():
    if SLOT_11:
        PaletteIndex(2)
    else:
        PaletteIndex(0)


@Subroutine
def Funnel_Disp():
    if SLOT_IsInHitstun:
        Visibility(1)
        DeleteObject(4)
        DeleteObject(5)
    elif SLOT_33:
        Visibility(1)
    elif SLOT_51:
        Visibility(1)
    else:
        Visibility(0)
        DespawnEAEffect('Funnel_Mhoujin')

    def upon_39():
        SLOT_51 = 1
        ObjectUpon(FALLING, 39)
        ObjectUpon(5, 39)

    def upon_40():
        SLOT_51 = 0
        ObjectUpon(FALLING, 40)
        ObjectUpon(5, 40)


@Subroutine
def TimeStop_Atk():
    if SLOT_11:
        IgnoreBurst(1)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpulseBeforeWallbounce(0)
        PushbackX(0)
        PassByArmor(1)
        DefeatOpponentBehavior(1)
        CounterHitSetting(1)
        NoAttackOffset(1)
        EnemyHitstopAddition(0, 9999, 9999)
        ShutUp(1)
        CopyFromRightToLeft(23, 2, 67, 22, 2, 38)
        if SLOT_IsFacingRight == SLOT_67:
            FlipOnHit(1)


@Subroutine
def Func_FunnelC():
    Unknown30007(1)
    Unknown30011('')
    Unknown30009(64)
    callSubroutine('Funnel_Pallet')
    DisableBarrier(1)
    AttackDefaults_Projectile()
    E0EAEffectPosition(3)
    CancelIfPlayerHit(3)
    RemoveOnCallStateEnd(3)
    if SLOT_11:
        callSubroutine('TimeStop_Atk')
    else:
        AttackDirection(2)
    UseSlashHitspark(1)
    AutoHitStopSending(1)
    WallCollisionDetection(1)
    EnableAfterimage(1)
    AttackOff()
    SLOT_33 = 120

    def upon_STATE_END():
        SLOT_33 = 0
    ContinueState(120)


@Subroutine
def Func_FunnelD():
    Unknown30007(1)
    Unknown30011('')
    Unknown30009(64)
    callSubroutine('Funnel_Pallet')
    DisableBarrier(1)
    Voiceline('mi110')
    AttackDefaults_Projectile()
    AttackP1(80)
    AttackP2(85)
    StarterRating(2)
    if SLOT_11:
        callSubroutine('TimeStop_Atk')
    else:
        AttackDirection(2)
        EnemyHitstopAddition(0, 5, 7)
    UseSlashHitspark(1)
    AutoHitSignalSending(0)
    AttackOff()
    TeleportToObject(3)
    AddX(100000)
    AddY(250000)
    ContinueState(150)

    def upon_PLAYER_DAMAGED():
        DeleteObject(23)

    def upon_PLAYER_BLOCKS():
        DeleteObject(23)

    def upon_OPPONENT_HIT_OR_BLOCK():
        AttackOff()
    RunLoopUpon(17, 180)

    def upon_17():
        DeleteObject(23)

    def upon_EVERY_FRAME():
        if not SLOT_33:
            DeleteObject(23)

    def upon_STATE_END():
        SLOT_33 = 0

    def upon_LANDING():
        sendToLabel(99)

    def upon_41():
        DeleteObject(23)


@State
def EMB():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(290000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emblem_mi', '')
        RenderLayer(5)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4278190335, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4294967295, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 80)


@State
def EMB_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(290000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emblem_mi', '')
        RenderLayer(5)
    sprite('null', 8)
    ColorForTransition(4278190080)
    ColorTransition(4294967295, 10)
    sprite('null', 8)
    ColorTransition(4286625023, 10)
    sprite('null', 8)
    ColorTransition(4278223103, 10)
    sprite('null', 8)
    ColorTransition(4278223103, 10)
    sprite('null', 80)


@State
def EMB_MI_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Eff3DEffect('ef_emblem_mi', '')
        RenderLayer(5)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294901760, 10)
    sprite('null', 10)
    ColorTransition(4294912040, 10)
    sprite('null', 10)
    ColorTransition(4294948020, 10)
    sprite('null', 10)
    ColorTransition(4294901760, 10)
    sprite('null', 80)


@State
def ModelMagicCircle1():

    def upon_IMMEDIATE():
        Visibility(1)
        Eff3DEffect('rgef_mc.DIG', 'rgef_mc_motion_000.mmot')
        FaceSpawnLocation()
        ColorFromPaletteIndex(224)
        IgnoreScreenfreeze(1)
    sprite('null', 74)


@Subroutine
def FU_ActReset():
    E0EAEffectPositionCenter(3)
    E0EAEffectDirection(3)
    IgnorePauses(3)
    RemoveOnContact(3)
    IgnoreScreenfreeze(1)
    SetZVal(500)

    def upon_STATE_END():
        EndMomentum(1)
        XPositionRelativeFacing(0)
        AbsoluteY(0)
    uponSendToLabel(41, 99)
    callSubroutine('FunnelSignalSetup')


@Subroutine
def FunnelSignalSetup():

    def upon_VALUE_RECEIVED():
        if SLOT_ReceivedValue == 100:
            PrivateFunction2('FunnelNeutral', 900)
        if SLOT_ReceivedValue == 1100:
            PrivateFunction2('FunnelNeutral_Open', 900)
        if SLOT_ReceivedValue == 101:
            PrivateFunction2('FunnelReaction', 1000)
        if SLOT_ReceivedValue == 103:
            PrivateFunction2('FunnelTurn', 1000)
        if SLOT_ReceivedValue == 1103:
            PrivateFunction2('FunnelTurn_Open', 1000)
        if SLOT_ReceivedValue == 132:
            PrivateFunction2('FunnelFDash', 1000)
        if SLOT_ReceivedValue == 311:
            PrivateFunction2('FunnelFThrow', 1000)
        if SLOT_ReceivedValue == 313:
            PrivateFunction2('FunnelBThrow', 1000)
        if SLOT_ReceivedValue == 321:
            PrivateFunction2('FunnelAThrow', 1000)
        if SLOT_ReceivedValue == 333:
            PrivateFunction2('FunnelOD', 2000)
        if SLOT_ReceivedValue == 404:
            PrivateFunction2('FunnelBarrier', 1000)
        if SLOT_ReceivedValue == 1404:
            PrivateFunction2('FunnelBarrier_Open', 1000)
        if SLOT_ReceivedValue == 203:
            PrivateFunction2('Funnel5D', 1000)
        if SLOT_ReceivedValue == 204:
            PrivateFunction2('Funnel5DD', 1000)
        if SLOT_ReceivedValue == 205:
            PrivateFunction2('Funnel6D', 1000)
        if SLOT_ReceivedValue == 206:
            PrivateFunction2('Funnel4D', 1000)
        if SLOT_ReceivedValue == 207:
            PrivateFunction2('Funnel2D', 1000)
        if SLOT_ReceivedValue == 407:
            PrivateFunction2('FunnelLaser', 1000)
        if SLOT_ReceivedValue == 408:
            PrivateFunction2('FunnelSaws', 1000)
        if SLOT_ReceivedValue == 431:
            PrivateFunction2('FunnelTimeStopThrow', 1000)
        if SLOT_ReceivedValue == 1431:
            PrivateFunction2('FunnelTimeStopThrow_Open', 1000)
        if SLOT_ReceivedValue == 615:
            PrivateFunction2('FunnelRoundWin', 1000)
        if SLOT_ReceivedValue == 611:
            PrivateFunction2('FunnelMatchWin2', 1000)


@State
def FunnelCreate():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')
        clearUponHandler(41)
    Unknown30007(1)
    Unknown30011('')
    Unknown30009(64)
    sprite('null', 1)
    sprite('null', 10)
    enterState('FunnelNeutral')


@State
def FunnelNeutral():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')
        clearUponHandler(41)
        uponSendToLabel(33, 1)
        E0EAEffectPositionCenter(0)

        def upon_EVERY_FRAME():
            CopyFromRightToLeft(23, 2, 60, 3, 2, 60)
            if SLOT_60 == 1:
                PrivateFunction3(3, 0, 150000, 100, 0)
            if SLOT_60 == 2:
                PrivateFunction3(3, 0, 0, 100, 0)
            if SLOT_60 == 3:
                PrivateFunction3(3, 0, 50000, 100, 0)
            if not SLOT_60:
                if not SLOT_60 == 3:
                    PrivateFunction3(3, 0, 200000, 100, 0)
                else:
                    PrivateFunction3(3, 0, 50000, 100, 0)
            if SLOT_33:
                SetActionMark(1)
            elif SLOT_2:
                CreateObject('mi408_CreateEff', -1)
                SetActionMark(0)
            callSubroutine('Funnel_Disp')
            callSubroutine('Funnel_Pallet')
    label(1)
    sprite('mi000_f00', 6)
    loopRest()
    if not SLOT_IsFacingRight:
        notConditionalSendToLabel(10)
    label(0)
    sprite('mi000_f11', 6)
    sprite('mi000_f10', 6)
    sprite('mi000_f09', 6)
    sprite('mi000_f08', 6)
    sprite('mi000_f07', 6)
    sprite('mi000_f06', 6)
    sprite('mi000_f05', 6)
    sprite('mi000_f04', 6)
    sprite('mi000_f03', 6)
    sprite('mi000_f02', 6)
    sprite('mi000_f01', 6)
    sprite('mi000_f00', 6)
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('mi000_f00', 6)
    sprite('mi000_f01', 6)
    sprite('mi000_f02', 6)
    sprite('mi000_f03', 6)
    sprite('mi000_f04', 6)
    sprite('mi000_f05', 6)
    sprite('mi000_f06', 6)
    sprite('mi000_f07', 6)
    sprite('mi000_f08', 6)
    sprite('mi000_f09', 6)
    sprite('mi000_f10', 6)
    sprite('mi000_f11', 6)
    loopRest()
    gotoLabel(1)


@State
def FunnelNeutral_Open():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')
        clearUponHandler(41)
        CreateObject('FunnelThudenrEff', -1)
        RegisterObject(4, 1)
        CreateObject('FunnelThudenrEffSub', -1)
        RegisterObject(5, 1)

        def upon_32():
            CreateObject('Funnel_Mhoujin', -1)

        def upon_EVERY_FRAME():
            CopyFromRightToLeft(23, 2, 60, 3, 2, 60)
            if SLOT_60 == 1:
                PrivateFunction3(3, 0, 130000, 100, 0)
            if SLOT_60 == 2:
                PrivateFunction3(3, 0, 80000, 100, 0)
            if SLOT_60 == 3:
                PrivateFunction3(3, 0, 100000, 100, 0)
            if not SLOT_60:
                if not SLOT_60 == 3:
                    PrivateFunction3(3, 0, 160000, 100, 0)
                else:
                    PrivateFunction3(3, 0, 100000, 100, 0)
            callSubroutine('Funnel_Disp')
            callSubroutine('Funnel_Pallet')

        def upon_45():
            if not SLOT_7:
                PrivateFunction2('FunnelNeutral', 100)
    label(0)
    sprite('mi000_f12ex00', 3)
    sprite('mi000_f12ex01', 3)
    sprite('mi000_f12ex02', 3)
    sprite('mi000_f12ex03', 3)
    loopRest()
    gotoLabel(0)


@State
def FunnelReaction():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')

        def upon_EVERY_FRAME():
            if SLOT_33:
                SetActionMark(1)
            elif SLOT_2:
                CreateObject('mi408_CreateEff', -1)
                SetActionMark(0)
            callSubroutine('Funnel_Disp')
    sprite('mi001_f00', 4)
    sprite('mi001_f01', 10)
    sprite('mi001_f02', 4)
    sprite('mi001_f03', 4)
    sprite('mi001_f04', 60)
    Voiceline('mi000')
    sprite('mi001_f05', 6)
    sprite('mi001_f06', 6)
    sprite('mi001_f07', 6)
    sprite('mi000_f00', 12)
    label(99)
    sprite('keep', 10)
    PrivateFunction2('FunnelNeutral', 100)


@State
def FunnelThudenrEffTenkai():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        ParticleLayer(11)
        Eff3DEffect('mieff_bitchange00', '')
        TeleportToObject(3)
        if not SLOT_60 == 3:
            AddY(180000)
        else:
            AddY(130000)
        E0EAEffectPosition(3)
    sprite('null', 20)
    CreateParticle('mief402_tenakieff', 100)
    ConstantAlphaModifier(-12)
    if SLOT_11:
        PaletteIndex(2)
        ColorFromPaletteIndex(64)
    else:
        PaletteIndex(0)
        ColorFromPaletteIndex(64)


@State
def Funnel_Mhoujin():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnContact(3)
        E0EAEffectDirection(3)
        CancelIfPlayerHit(3)
        IgnoreScreenfreeze(1)
        callSubroutine('Funnel_Pallet')

        def upon_EVERY_FRAME():
            CopyFromRightToLeft(23, 2, 60, 3, 2, 60)
            if SLOT_60 == 1:
                PrivateFunction3(3, 0, 130000, 100, 0)
            if SLOT_60 == 2:
                PrivateFunction3(3, 0, 80000, 100, 0)
            if not SLOT_60:
                if not SLOT_60 == 2:
                    PrivateFunction3(3, 0, 160000, 100, 0)
                else:
                    PrivateFunction3(3, 0, 100000, 100, 0)
            if SLOT_33:
                if SLOT_33 <= 5:
                    sendToLabel(9)
                    clearUponHandler(EVERY_FRAME)

        def upon_STATE_END():
            SLOT_33 = 0
    sprite('mi000_f12ex30', 3)
    Visibility(1)
    CreateObject('BitEffct', 0)
    CreateObject('BitEffct', 1)
    CreateObject('BitEffct', 2)
    sprite('mi000_f12ex31', 3)
    sprite('mi000_f12ex32', 3)
    Visibility(0)
    sprite('mi000_f12ex33', 3)
    label(0)
    sprite('mi000_f12ex30', 3)
    sprite('mi000_f12ex31', 3)
    sprite('mi000_f12ex32', 3)
    sprite('mi000_f12ex33', 3)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('keep', 5)
    Visibility(1)
    CreateObject('BitEffct', 0)
    CreateObject('BitEffct', 1)
    CreateObject('BitEffct', 2)


@State
def BitEffct():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnContact(3)
        E0EAEffectDirection(3)
        LinkParticle('mief_bitDel2')
    sprite('null', 40)
    PrivateSE('mise_16')


@State
def FunnelThudenrEff():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RenderLayer(5)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        RemoveOnContact(2)
        E0EAEffectDirection(2)
        Eff3DEffect('mieff_bitatk00', '')
        if SLOT_11:
            PaletteIndex(2)
            ColorFromPaletteIndex(64)
        else:
            PaletteIndex(0)
            ColorFromPaletteIndex(64)

        def upon_32():
            PaletteIndex(2)
            ColorFromPaletteIndex(64)

        def upon_33():
            PaletteIndex(0)
            ColorFromPaletteIndex(64)

        def upon_39():
            AlphaValue(0)

        def upon_40():
            AlphaValue(255)
    sprite('null', 32767)


@State
def FunnelThudenrEffSub():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RenderLayer(5)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        RemoveOnContact(2)
        E0EAEffectDirection(2)
        Eff3DEffect('mieff_bitatk01', '')

        def upon_39():
            AlphaValue(0)

        def upon_40():
            AlphaValue(255)
    sprite('null', 32767)


@State
def FunnelEmptyEff():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        LinkParticle('mief_emptybit')
    sprite('null', 32767)


@State
def FunnelThudenrEffShunou():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        ParticleLayer(11)
        Eff3DEffect('mieff408_deleff01', '')
        PaletteIndex(0)
        ColorFromPaletteIndex(64)
        ParticleColorFromPalette(64, 64, 64)
        CallPrivateEffect('mief403_shunoieff')
        TeleportToObject(3)
        AddX(-54000)
        Size(1150)
        if not SLOT_33 <= 5:
            AddY(360000)
        else:
            AddY(260000)
        E0EAEffectPosition(3)
    sprite('null', 20)
    CreateParticle('mief403_shunoieff_tb', -1)
    ConstantAlphaModifier(-12)
    if SLOT_11:
        PaletteIndex(2)
        ColorFromPaletteIndex(64)
    else:
        PaletteIndex(0)
        ColorFromPaletteIndex(64)


@State
def FunnelTurn():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')

        def upon_EVERY_FRAME():
            if SLOT_33:
                SetActionMark(1)
            elif SLOT_2:
                CreateObject('mi408_CreateEff', -1)
                SetActionMark(0)
            callSubroutine('Funnel_Disp')
    sprite('mi003_f00', 3)
    sprite('mi003_f01', 3)
    sprite('mi003_f00ex01', 3)
    label(99)
    sprite('keep', 10)
    PrivateFunction2('FunnelNeutral', 100)


@State
def FunnelTurn_Open():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')
        CreateObject('FunnelThudenrEff2', -1)
        RegisterObject(4, 1)
        CreateObject('FunnelThudenrEff2Sub', -1)
        RegisterObject(5, 1)

        def upon_32():
            CreateObject('Funnel_Mhoujin', -1)

        def upon_EVERY_FRAME():
            callSubroutine('Funnel_Disp')
            callSubroutine('Funnel_Pallet')

        def upon_45():
            if not SLOT_7:
                PrivateFunction2('FunnelNeutral', 100)
    sprite('mi003_f02', 3)
    sprite('mi003_f03', 3)
    sprite('mi003_f02ex01', 3)
    label(99)
    sprite('keep', 10)
    PrivateFunction2('FunnelNeutral_Open', 100)


@State
def FunnelThudenrEff2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RenderLayer(5)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        RemoveOnContact(3)
        E0EAEffectDirection(2)
        Eff3DEffect('mieff_bitatk00', '')
    sprite('null', 3)
    if SLOT_11:
        PaletteIndex(2)
        ColorFromPaletteIndex(64)
    else:
        PaletteIndex(0)
        ColorFromPaletteIndex(64)
    AddX(60000)
    sprite('null', 3)
    sprite('null', 3)
    AddX(-60000)
    sprite('null', 10)


@State
def FunnelThudenrEff2Sub():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RenderLayer(5)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        RemoveOnContact(3)
        E0EAEffectDirection(2)
        Eff3DEffect('mieff_bitatk01', '')
    sprite('null', 3)
    AddX(60000)
    sprite('null', 3)
    sprite('null', 3)
    AddX(-60000)
    sprite('null', 10)


@State
def FunnelFDash():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')

        def upon_EVERY_FRAME():
            if SLOT_33:
                SetActionMark(1)
            elif SLOT_2:
                CreateObject('mi408_CreateEff', -1)
                SetActionMark(0)
            callSubroutine('Funnel_Disp')
    sprite('keep', 1)
    if not SLOT_IsFacingRight:
        notConditionalSendToLabel(10)
    label(0)
    sprite('mi032_f08', 3)
    sprite('mi032_f07', 3)
    sprite('mi032_f06', 3)
    sprite('mi032_f05', 3)
    sprite('mi032_f04', 3)
    sprite('mi032_f03', 3)
    sprite('mi032_f02', 3)
    sprite('mi032_f01', 3)
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('mi032_f01', 3)
    sprite('mi032_f02', 3)
    sprite('mi032_f03', 3)
    sprite('mi032_f04', 3)
    sprite('mi032_f05', 3)
    sprite('mi032_f06', 3)
    sprite('mi032_f07', 3)
    sprite('mi032_f08', 3)
    loopRest()
    gotoLabel(10)
    label(99)
    sprite('keep', 10)
    PrivateFunction2('FunnelNeutral', 100)


@State
def FunnelFThrow():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')

        def upon_EVERY_FRAME():
            callSubroutine('Funnel_Disp')

        def upon_STATE_END():
            SetScaleSpeed(0)
            Size(1000)
            AlphaValue(255)
            ConstantAlphaModifier(0)
    sprite('mi311_f00', 5)
    sprite('mi311_f01', 5)
    sprite('mi311_f02', 5)
    sprite('mi311_f03', 5)
    sprite('mi311_f04', 5)
    sprite('mi311_f05', 5)
    sprite('mi311_f06', 5)
    sprite('mi311_f07', 5)
    sprite('mi311_f08', 5)
    sprite('mi311_f08', 5)
    SetScaleSpeed(10)
    ConstantAlphaModifier(-20)
    sprite('mi311_f08', 20)
    SetScaleSpeed(0)
    sprite('mi311_f01', 15)
    SetScaleSpeed(0)
    Size(1000)
    ConstantAlphaModifier(20)
    sprite('mi311_f00', 5)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    label(99)
    sprite('keep', 10)
    PrivateFunction2('FunnelNeutral', 100)


@State
def FunnelBThrow():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')
        E0EAEffectDirection(0)

        def upon_EVERY_FRAME():
            callSubroutine('Funnel_Disp')

        def upon_STATE_END():
            SetScaleSpeed(0)
            Size(1000)
            AlphaValue(255)
            ConstantAlphaModifier(0)
    sprite('mi311_f00', 4)
    sprite('mi311_f01', 4)
    sprite('mi311_f02', 4)
    sprite('mi311_f03', 4)
    sprite('mi311_f04', 4)
    sprite('mi311_f05', 4)
    sprite('mi311_f06', 4)
    sprite('mi311_f07', 4)
    sprite('mi311_f08', 5)
    sprite('mi311_f08', 5)
    SetScaleSpeed(10)
    ConstantAlphaModifier(-20)
    sprite('mi311_f08', 23)
    SetScaleSpeed(0)
    sprite('mi311_f03', 4)
    SetScaleSpeed(0)
    Size(1000)
    ConstantAlphaModifier(20)
    sprite('mi311_f02', 4)
    sprite('mi311_f01', 4)
    sprite('mi311_f00', 4)
    AlphaValue(255)
    ConstantAlphaModifier(0)
    label(99)
    sprite('keep', 10)
    PrivateFunction2('FunnelNeutral', 100)


@State
def FunnelAThrow():

    def upon_IMMEDIATE():

        def upon_EVERY_FRAME():
            callSubroutine('Funnel_Disp')
        callSubroutine('FU_ActReset')
    sprite('mi321_f00', 4)
    sprite('mi321_f01', 4)
    sprite('mi321_f02', 5)
    sprite('mi321_f03', 3)
    sprite('mi321_f04', 3)
    sprite('mi321_f05', 3)
    sprite('mi321_f06', 3)
    sprite('mi321_f07', 3)
    sprite('mi321_f08', 3)
    sprite('mi321_f09', 3)
    sprite('mi321_f10', 3)
    sprite('mi321_f11', 3)
    label(99)
    sprite('keep', 10)
    PrivateFunction2('FunnelNeutral', 100)


@State
def FunnelOD():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')
        Visibility(1)
        DespawnEAEffect('FunnelThudenrEff')
        DespawnEAEffect('FunnelThudenrEffSub')
    sprite('null', 32767)
    label(99)
    sprite('keep', 10)
    SLOT_7 = 0
    PrivateFunction2('FunnelNeutral', 100)


@State
def FunnelBarrier():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')
        uponSendToLabel(32, 0)

        def upon_EVERY_FRAME():
            callSubroutine('Funnel_Disp')
            callSubroutine('Funnel_Pallet')
    sprite('mi003_f00ex01', 4)
    sprite('mi003_f01', 28)
    label(0)
    sprite('mi003_f00ex01', 3)
    label(99)
    sprite('keep', 10)
    PrivateFunction2('FunnelNeutral', 100)


@State
def FunnelBarrier_Open():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')
        CreateObject('FunnelThudenrEff3', -1)
        RegisterObject(4, 1)
        CreateObject('FunnelThudenrEff3Sub', -1)
        RegisterObject(5, 1)

        def upon_32():
            CreateObject('Funnel_Mhoujin', -1)

        def upon_EVERY_FRAME():
            E0EAEffectPositionCenter(0)
            PrivateFunction3(3, 0, 160000, 100, 0)
            callSubroutine('Funnel_Disp')
            callSubroutine('Funnel_Pallet')
    sprite('mi003_f02ex01', 4)
    sprite('mi404_f00', 28)
    sprite('mi003_f02ex01', 3)
    label(99)
    sprite('keep', 10)
    PrivateFunction2('FunnelNeutral_Open', 100)


@State
def FunnelThudenrEff3():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RenderLayer(5)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        RemoveOnContact(3)
        E0EAEffectDirection(2)
        Eff3DEffect('mieff_bitatk00', '')
    sprite('null', 32767)
    if SLOT_11:
        PaletteIndex(2)
        ColorFromPaletteIndex(64)
    else:
        PaletteIndex(0)
        ColorFromPaletteIndex(64)
    AddX(60000)


@State
def FunnelThudenrEff3Sub():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RenderLayer(5)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        RemoveOnContact(3)
        E0EAEffectDirection(2)
        Eff3DEffect('mieff_bitatk01', '')
    sprite('null', 32767)
    AddX(60000)


@State
def Funnel5D():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')
    sprite('mi203_f00', 3)
    PrivateSE('mise_00')
    sprite('mi203_f01', 3)
    sprite('mi203_f02', 3)
    sprite('mi203_f03', 3)
    sprite('mi203_f04', 3)
    label(99)
    sprite('keep', 10)
    SLOT_7 = 1
    PrivateFunction2('FunnelNeutral_Open', 100)


@State
def Funnel5DD():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')
        SLOT_7 = 0
    sprite('mi204_f00', 4)
    PrivateSE('mise_00')
    sprite('mi204_f01', 4)
    sprite('mi204_f02', 4)
    sprite('mi204_f03', 4)
    sprite('mi204_f04', 4)
    label(99)
    sprite('keep', 10)
    SLOT_7 = 0
    PrivateFunction2('FunnelNeutral', 100)


@State
def Funnel6D():

    def upon_IMMEDIATE():
        callSubroutine('Func_FunnelD')
        AttackLevel_(2)
        Damage(400)
        Hitstop(3)
        if not SLOT_11:
            PushbackX(30400)
        AddX(-50000)
        WallCollisionDetection(1)
        Unknown1111(12000, 22)
        CopyFromRightToLeft(23, 2, 51, 3, 2, 23)
        CopyFromRightToLeft(23, 2, 52, 22, 2, 23)
        if not op(1, 2, 51, 2, 52):
            RotationAngle(0)
            physicsXImpulse(12000)
            physicsYImpulse(0)
        XImpulseAcceleration(10)
        YAccel(10)
        HitsPerCall(3, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            sendToLabel(1)
    sprite('mi203_f08ex01', 2)
    AlphaValue(0)
    ConstantAlphaModifier(10)
    RenderLayer(1)
    CreateObject('mi408_DelEff', -1)
    PrivateSE('mise_05')
    sprite('mi203_f09ex01', 1)
    sprite('mi203_f09ex01', 1)
    clearUponHandler(41)
    sprite('mi203_f10ex01', 2)
    sprite('mi203_f08ex01', 2)
    sprite('mi203_f09ex01', 2)
    sprite('mi203_f10ex01', 2)
    sprite('mi203_f08ex01', 2)
    sprite('mi203_f09ex01', 2)
    sprite('mi203_f10ex01', 2)
    sprite('mi203_f08ex01', 2)
    sprite('mi203_f09ex01', 2)
    sprite('mi203_f10ex01', 2)
    sprite('mi203_f08ex01', 2)
    sprite('mi203_f09ex01', 2)
    sprite('mi203_f10ex01', 2)
    sprite('mi203_f08ex01', 2)
    sprite('mi203_f09ex01', 2)
    sprite('mi203_f10ex01', 2)
    RenderLayer(0)
    CreateObject('mi6DParticle', -1)
    CreateObject('mi6DWind', -1)
    sprite('mi203_f08', 2)
    TriggerUponForState('mi6DParticle', 32)
    RefreshMultihit()
    XImpulseAcceleration(4000)
    YAccel(4000)
    sprite('mi203_f09', 2)
    RefreshMultihit()
    sprite('mi203_f10', 2)
    RefreshMultihit()
    WallCollisionDetection(0)
    label(0)
    sprite('mi203_f08', 2)
    RefreshMultihit()
    sprite('mi203_f09', 2)
    RefreshMultihit()
    sprite('mi203_f10', 2)
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mi203_f08ex01', 4)
    clearUponHandler(LANDING)
    XImpulseAcceleration(50)
    YAccel(50)
    ConstantAlphaModifier(-10)
    DespawnEAEffect('mi6DParticle')
    DespawnEAEffect('mi6DWind')
    sprite('mi203_f09ex01', 4)
    XImpulseAcceleration(50)
    YAccel(50)
    ConstantAlphaModifier(-10)
    sprite('mi203_f10ex01', 4)
    XImpulseAcceleration(50)
    YAccel(50)
    ConstantAlphaModifier(-10)
    loopRest()
    gotoLabel(1)
    label(99)
    sprite('null', 32767)
    clearUponHandler(54)
    EndMomentum(1)
    AttackOff()
    CreateObject('mi408_DelEff', -1)
    TriggerUponForState('mi6DWind', 32)
    DespawnEAEffect('mi6DParticle')


@State
def mi6DWind():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AlphaValue(230)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        callSubroutine('Funnel_Pallet')
        E0EAEffectRotation(2)
        Eff3DEffect('mieff6D_wind00', '')
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 3)
    AddScaleY(-350)
    sprite('null', 3)
    AddScaleY(350)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    ConstantAlphaModifier(-40)
    loopRest()


@State
def mi6DParticle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        callSubroutine('Funnel_Pallet')
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 4)
    ParticleSize(900)
    ParticleColorFromPalette(64, 64, 64)
    CallCustomizableParticle('mief_bitnokosi_back3', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    ParticleSize(900)
    ParticleColorFromPalette(64, 64, 64)
    CallCustomizableParticle('mief_bitnokosi_back3', -1)
    gotoLabel(1)


@State
def Funnel4D():

    def upon_IMMEDIATE():
        callSubroutine('Func_FunnelD')
        AttackLevel_(1)
        Damage(400)
        Hitstop(0)
        if not SLOT_11:
            PushbackX(19800)

        def upon_32():
            AddX(-100000)
            AddY(180000)
            PrivateSE('mise_06')

        def upon_33():
            AddX(40000)
            AddY(-100000)

        def upon_34():
            AddX(-260000)
            AddY(-150000)
        E0EAEffectPosition(3)
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            sendToLabel(1)
    sprite('null', 1)
    sprite('mi203_f05', 2)
    CreateObject('mi4DParticle', -1)
    sprite('mi203_f05', 6)
    clearUponHandler(41)
    sprite('mi203_f05ex01', 4)
    physicsXImpulse(10000)
    RefreshMultihit()
    TriggerUponForState('mi4DParticle', 32)
    sprite('mi203_f05ex02', 4)
    E0EAEffectPosition(0)
    XImpulseAcceleration(600)
    sprite('mi203_f05ex01', 4)
    sprite('mi203_f05ex02', 4)
    sprite('mi203_f05ex01', 4)
    loopRest()
    gotoLabel(99)
    label(1)
    sprite('mi203_f05', 4)
    clearUponHandler(LANDING)
    XImpulseAcceleration(60)
    YAccel(60)
    ConstantAlphaModifier(-10)
    DespawnEAEffect('mi4DParticle')
    loopRest()
    gotoLabel(1)
    label(99)
    sprite('null', 32767)
    EndMomentum(1)
    AttackOff()
    CreateObject('miBit_DelEff', -1)
    DespawnEAEffect('mi4DParticle')


@State
def mi4DParticle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        callSubroutine('Funnel_Pallet')
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 4)
    ParticleSize(600)
    ParticleColorFromPalette(64, 64, 64)
    CallCustomizableParticle('mief_bitnokosi_back3', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    ParticleSize(600)
    ParticleColorFromPalette(64, 64, 64)
    CallCustomizableParticle('mief_bitnokosi_back3', -1)
    gotoLabel(1)


@State
def Funnel2D():

    def upon_IMMEDIATE():
        callSubroutine('Func_FunnelD')
        AttackLevel_(1)
        Damage(400)
        Hitstop(0)
        if not SLOT_11:
            PushbackX(19800)

        def upon_32():
            RotationAngle(20000)
            XSpeed2(1000, 0)
            CreateObject('miBit_DelEff', -1)
            PrivateSE('mise_05')

        def upon_33():
            RotationAngle(40000)
            XSpeed2(1000, 0)
            SLOT_51 = 1

        def upon_34():
            RotationAngle(0)
            XSpeed2(1000, 0)
            SLOT_52 = 1

        def upon_35():
            RotationAngle(0)
            XSpeed2(1000, 0)
            CreateObject('mi408_DelEff', -1)
            PrivateSE('mise_05')

        def upon_36():
            RotationAngle(20000)
            XSpeed2(1000, 0)
            SLOT_51 = 1

        def upon_37():
            RotationAngle(-20000)
            XSpeed2(1000, 0)
            SLOT_52 = 1

        def upon_38():
            RotationAngle(-20000)
            XSpeed2(1000, 0)
            CreateObject('mi408_DelEff', -1)
            PrivateSE('mise_05')

        def upon_39():
            RotationAngle(0)
            XSpeed2(1000, 0)
            SLOT_51 = 1

        def upon_40():
            RotationAngle(-40000)
            XSpeed2(1000, 0)
            SLOT_52 = 1
        HitsPerCall(1, 1, 1, 1, 1, 0, 0, 0)

        def upon_54():
            sendToLabel(1)
    sprite('mi203_f05', 3)
    Visibility(1)
    sprite('mi203_f05', 2)
    clearUponHandler(41)
    sprite('mi203_f05', 4)
    SpriteCall('mi203_f05', 3, 2, 51)
    SpriteCall('mi203_f05', 5, 2, 52)
    CreateObject('mi4DParticle', -1)
    sprite('mi203_f05ex01', 4)
    RefreshMultihit()
    XImpulseAcceleration(1000)
    YAccel(1000)
    Visibility(0)
    TriggerUponForState('mi4DParticle', 32)
    sprite('mi203_f05ex02', 4)
    XImpulseAcceleration(500)
    YAccel(500)
    label(0)
    sprite('mi203_f05ex01', 4)
    sprite('mi203_f05ex02', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('mi203_f05', 8)
    clearUponHandler(LANDING)
    XImpulseAcceleration(60)
    YAccel(60)
    ConstantAlphaModifier(-10)
    DespawnEAEffect('mi4DParticle')
    loopRest()
    gotoLabel(1)
    label(99)
    sprite('null', 32767)
    clearUponHandler(54)
    EndMomentum(1)
    AttackOff()
    CreateObject('miBit_DelEff', -1)
    DespawnEAEffect('mi4DParticle')


@State
def miBit_DelEff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        ParticleLayer(11)
        CallPrivateEffect('mief408_del')
        Size(700)
    sprite('null', 60)
    CreateObject('miBit_DelEffSub', -1)


@State
def miBit_DelEffSub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        RenderLayer(5)
        Eff3DEffect('mieff408_deleff00', '')
        E0EAEffectScale(2)
        Size(600)
    sprite('null', 20)
    CreateObject('miBit_DelEffSub2', -1)
    sprite('null', 10)
    ConstantAlphaModifier(-25)


@State
def miBit_DelEffSub2():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        Size(1200)
        AddRotationPerFrame(15000)
        RenderLayer(11)
    sprite('vrmi408_yugami', 15)
    ParticleTransparency(1)
    PlayerTransparency(50000)
    Unknown3059(-2000)
    SetScaleSpeed(-20)


@State
def Funnel5C():

    def upon_IMMEDIATE():
        callSubroutine('Func_FunnelC')
        AttackLevel_(3)
        Damage(600)
        Hitstop(7)
        if not SLOT_11:
            GroundedHitstunAnimation(2)
            AirUntechableTime(29)
            AirPushbackY(20000)
            AirPushbackX(30000)
            CHFloorslide(10)
        AddY(180000)
        SetZVal(500)
    sprite('mi202_f00', 2)
    sprite('mi202_f01', 3)
    sprite('mi202_f02', 3)
    physicsXImpulse(3000)
    SetAcceleration(300)
    physicsYImpulse(-8000)
    sprite('mi202_f03', 4)
    CreateObject('mi232Particle', 0)
    XImpulseAcceleration(200)
    YAccel(50)
    IgnorePauses(0)
    E0EAEffectPosition(0)
    CommonSE('006_swing_blade_2')
    sprite('mi202_f04', 8)
    XImpulseAcceleration(600)
    YAccel(0)
    CreateObject('mi232Particle', 1)
    RefreshMultihit()
    sprite('mi202_f04', 3)
    ConstantAlphaModifier(-20)
    XImpulseAcceleration(30)
    sprite('mi202_f05', 10)
    XImpulseAcceleration(0)
    EnableAfterimage(0)
    DespawnEAEffect('mi232Particle')


@State
def Funnel2C():

    def upon_IMMEDIATE():
        callSubroutine('Func_FunnelC')
        AttackLevel_(3)
        Damage(600)
        Hitstop(7)
        if not SLOT_11:
            GroundedHitstunAnimation(6)
            AirHitstunAnimation(18)
            PushbackX(-39900)
            AirPushbackX(-6000)
            AirUntechableTime(31)
        AddY(80000)
        SetZVal(500)
    sprite('mi232_f00', 2)
    sprite('mi232_f01', 2)
    sprite('mi232_f02', 2)
    physicsXImpulse(50000)
    SetAcceleration(-1000)
    sprite('mi232_f03', 2)
    CreateObject('mi232Particle', 0)
    IgnorePauses(0)
    E0EAEffectPosition(0)
    sprite('mi232_f04', 2)
    CreateObject('mi232Particle', 0)
    sprite('mi232_f05', 2)
    sprite('mi232_f06', 4)
    SetZVal(-500)
    CommonSE('006_swing_blade_2')
    sprite('mi232_f07', 4)
    physicsXImpulse(0)
    SetAcceleration(-5000)
    sprite('mi232_f08', 6)
    RefreshMultihit()
    sprite('mi232_f09', 4)
    DespawnEAEffect('mi232Particle')
    AlphaValue(200)
    ConstantAlphaModifier(-10)
    XImpulseAcceleration(50)
    sprite('mi232_f09', 2)
    XImpulseAcceleration(50)
    sprite('mi232_f09', 2)
    EndMomentum(1)


@State
def Funnel6C():

    def upon_IMMEDIATE():
        callSubroutine('Func_FunnelC')
        AttackLevel_(4)
        Damage(600)
        BonusProration(110)
        if not SLOT_11:
            GroundedHitstunAnimation(11)
            AirHitstunAnimation(11)
            AirPushbackX(0)
            AirPushbackY(-60000)
            HardKnockdown(10)
            Floorslide(1)
            Hitstop(8)
        AddY(200000)
        SetZVal(500)

        def upon_EVERY_FRAME():
            if SLOT_YDistanceFromFloor <= 0:
                EndMomentum(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            XImpulseAcceleration(10)
            YAccel(10)
    sprite('mi212_f00', 4)
    sprite('mi212_f01', 3)
    physicsXImpulse(16000)
    physicsYImpulse(-2500)
    SetZVal(0)
    CommonSE('006_swing_blade_2')
    sprite('mi212_f02', 3)
    XImpulseAcceleration(80)
    YAccel(200)
    sprite('mi212_f03', 3)
    XImpulseAcceleration(80)
    YAccel(300)
    sprite('mi212_f04', 3)
    XImpulseAcceleration(80)
    YAccel(400)
    AttackOff()
    sprite('mi212_f04', 6)
    RefreshMultihit()
    E0EAEffectPosition(0)
    sprite('mi212_f05', 2)
    EndMomentum(1)
    sprite('mi212_f06', 2)
    sprite('mi212_f07', 2)
    sprite('mi212_f08', 2)
    sprite('mi212_f09', 2)
    AlphaValue(200)
    ConstantAlphaModifier(-10)
    sprite('mi212_f10', 2)
    sprite('mi212_f11', 2)
    sprite('mi212_f12', 2)


@State
def FunnelAir5C():

    def upon_IMMEDIATE():
        callSubroutine('Func_FunnelC')
        AttackLevel_(3)
        Damage(600)
        AttackP1(80)
        MoveAttributes(1, 0, 0, 0, 0)
        if not SLOT_11:
            AirPushbackY(-40000)
            AirUntechableTime(30)
        WallCollisionDetection(0)
        AddY(180000)
        SetZVal(0)
        IgnorePauses(3)
        RemoveOnCallStateEnd(3)

        def upon_OPPONENT_HIT_OR_BLOCK():
            RemoveOnCallStateEnd(0)

        def upon_EVERY_FRAME():
            CopyFromRightToLeft(23, 2, 52, 3, 2, 52)
            if not SLOT_52:
                DeleteObject(23)
    sprite('mi252_f00', 2)
    CommonSE('006_swing_blade_2')
    sprite('mi252_f01', 2)
    sprite('mi252_f02', 3)
    physicsXImpulse(40000)
    SetAcceleration(-2000)
    physicsYImpulse(-36000)
    setGravity(-4000)
    CreateObject('mi252Particle', 0)
    sprite('mi252_f03', 6)
    RefreshMultihit()
    sprite('mi252_f04', 6)
    IgnorePauses(0)
    AttackOff()
    physicsXImpulse(14500)
    SetAcceleration(-3000)
    physicsYImpulse(-6000)
    setGravity(-3000)
    ConstantAlphaModifier(-20)
    DespawnEAEffect('mi252Particle')
    sprite('mi252_f05', 6)
    E0EAEffectPosition(0)
    EndMomentum(1)


@State
def FuncAir2C():

    def upon_IMMEDIATE():
        TeleportToObject(3)
        EnableAfterimage(1)
        Unknown30007(1)
        Unknown30011('')
        Unknown30009(64)
        E0EAEffectPosition(3)
        IgnorePauses(3)
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        AddY(180000)
        AddX(32500)

        def upon_32():
            DeleteObject(23)
        if SLOT_11:
            PaletteIndex(2)
    label(0)
    sprite('mi254_f06', 2)
    PrivateSE('mise_03')
    sprite('mi254_f07', 2)
    sprite('mi254_f08', 2)
    PrivateSE('mise_03')
    sprite('mi254_f09', 2)
    sprite('mi254_f10', 2)
    PrivateSE('mise_03')
    sprite('mi254_f11', 2)
    sprite('mi254_f12', 2)
    PrivateSE('mise_03')
    sprite('mi254_f13', 2)
    sprite('mi254_f14', 2)
    loopRest()
    gotoLabel(0)


@State
def FunnelLaser():

    def upon_IMMEDIATE():
        Unknown30007(1)
        Unknown30011('')
        Unknown30009(64)
        AttackDefaults_SpecialProjectile()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        Hitstop(0)
        EnemyHitstopAddition(12, 12, 14)
        StarterRating(2)
        Unknown12052(1)
        if SLOT_11:
            callSubroutine('TimeStop_Atk')
        else:
            AirHitstunAnimation(14)
            GroundedHitstunAnimation(14)
            AirUntechableTime(46)
            AirPushbackX(2000)
            AirPushbackY(20000)
            PushbackX(0)
        E0EAEffectPosition(3)
        AddX(20000)
        AddY(200000)

        def upon_45():
            if SLOT_33 <= 10:
                SLOT_33 = 10

        def upon_STATE_END():
            RenderLayer(0)
            SLOT_7 = 0
            SLOT_33 = 0
        if SLOT_11:
            PaletteIndex(2)

        def upon_PLAYER_DAMAGED():
            DeleteObject(23)
        Unknown23170('ShotLaser')
    if SLOT_7:
        conditionalSendToLabel(0)
    sprite('mi407_f00', 3)
    PrivateSE('mise_06')
    sprite('mi407_f01', 3)
    sprite('mi407_f02', 3)
    RenderLayer(6)
    sprite('mi407_f03', 3)
    sprite('mi407_f04', 3)
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('mi203_f02', 5)
    RenderLayer(2)
    E0EAEffectPosition(0)
    PrivateSE('mise_06')
    sprite('mi203_f01', 5)
    sprite('mi203_f00', 5)
    loopRest()
    label(1)
    sprite('null', 1)
    E0EAEffectPosition(0)
    Voiceline('mi211')
    EffectPosition(22, 103)
    sprite('mi407_f05', 10)
    Visibility(1)
    CreateObject('miBit_DelEff', 0)
    PrivateSE('mise_10')
    CreateObject('miBit_DelEff', 1)
    CreateObject('miBit_DelEff', 2)
    sprite('mi407_f05', 3)
    Visibility(0)

    def upon_EVERY_FRAME():
        PrivateFunction3(22, 0, 0, 30, 1)
        if SLOT_YDistanceFromFloor <= 200000:
            SLOT_YDistanceFromFloor = 200000
    sprite('mi407_f06', 3)
    sprite('mi407_f07', 3)
    sprite('mi407_f08', 3)
    sprite('mi407_f05', 3)
    sprite('mi407_f06', 3)
    sprite('mi407_f07', 3)
    sprite('mi407_f08', 3)
    sprite('mi407_f05', 3)
    uponSendToLabel(RELEASE_D, 9)
    sprite('mi407_f06', 3)
    sprite('mi407_f07', 3)
    sprite('mi407_f08', 3)
    sprite('mi407_f05', 3)
    sprite('mi407_f06', 3)
    sprite('mi407_f07', 3)
    sprite('mi407_f08', 3)
    sprite('mi407_f05', 3)
    label(9)
    sprite('mi407_f10', 3)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(RELEASE_D)
    sprite('mi407_f11', 3)
    sprite('mi407_f12', 3)
    sprite('mi407_f13', 3)
    sprite('mi407_f05ex01', 4)
    EnableAfterimage(0)
    CommonSE('014_electric_ml')
    CommonSE('014_electric_sl')
    sprite('mi407_f05ex01', 6)
    EndAttack()
    sprite('mi407_f05ex02', 2)
    sprite('mi407_f05ex03', 2)
    sprite('mi407_f05ex04', 2)
    sprite('mi407_f05ex05', 2)
    sprite('mi407_f05ex06', 2)
    sprite('mi407_f13', 10)
    sprite('mi407_f13', 31)
    Visibility(1)
    CreateObject('mi408_DelEff', 0)

    def RunOnObject_1():
        Size(825)
    CreateObject('mi408_DelEff', 1)

    def RunOnObject_1():
        Size(825)
    CreateObject('mi408_DelEff', 2)

    def RunOnObject_1():
        Size(825)


@State
def FunnelSaws():

    def upon_IMMEDIATE():
        Unknown30007(1)
        Unknown30011('')
        Unknown30009(64)
        AttackDefaults_SpecialProjectile()
        AttackLevel_(2)
        Damage(300)
        AttackP1(80)
        AttackP2(75)
        SingleProration(1)
        Hitstop(1)
        StarterRating(2)
        Unknown12052(1)
        UseSlashHitspark(1)
        HitsparkSize(500)
        AttackOff()
        if SLOT_11:
            callSubroutine('TimeStop_Atk')
        else:
            AirPushbackY(10000)
            PushbackX(12000)
            AirUntechableTime(25)
        TeleportToObject(3)
        AddY(300000)
        AddX(150000)

        def upon_EVERY_FRAME():
            if SLOT_StateDuration >= 90:
                SetActionMark(0)
                sendToLabel(9)
            if SLOT_51:
                if CheckInput(INPUT_HOLD_D):
                    if CheckInput(0x92):
                        if not SLOT_2:
                            SLOT_2 = 1
                            YSpeed(5000)
                    elif CheckInput(0x44):
                        if not SLOT_2:
                            SLOT_2 = 1
                            YSpeed(-5000)
                    else:
                        SLOT_2 = 0
                        YSpeed(0)
                else:
                    SLOT_51 = 0
            if SLOT_YDistanceFromFloor <= 100000:
                AbsoluteY(100000)

        def upon_45():
            if SLOT_33 <= 10:
                SLOT_33 = 10
        HitsPerCall(6, 1, 1, 1, 1, 0, 0, 0)
        uponSendToLabel(54, 9)

        def upon_STATE_END():
            SLOT_7 = 0
            SLOT_33 = 0
        if SLOT_11:
            PaletteIndex(2)

        def upon_PLAYER_DAMAGED():
            DeleteObject(23)
        Unknown23170('ShotSaws')
    sprite('null', 5)
    SpriteIfNot0(20, 2, 7)
    CreateObject('mi408_DelEff', 0)
    PrivateSE('mise_05')
    sprite('mi408_f04', 2)
    Voiceline('mi212')
    RenderLayer(6)
    physicsXImpulse(14000)
    physicsYImpulse(-20000)
    setGravity(-1500)
    sprite('mi408_f05', 2)
    sprite('mi408_f06', 2)
    RefreshMultihit()
    CommonSE('006_swing_blade_1')
    sprite('mi408_f07', 2)
    SLOT_51 = 1

    def upon_RELEASE_D():
        SLOT_52 = 1
    label(0)
    sprite('mi408_f04', 2)
    if SLOT_52:
        XImpulseAcceleration(50)
    if not SLOT_51:
        YAccel(70)
    YAccel(70)
    PerGravity(50)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    sprite('mi408_f05', 2)
    sprite('mi408_f06', 2)
    RefreshMultihit()
    CommonSE('006_swing_blade_0')
    sprite('mi408_f07', 2)
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('mi408_f06', 1)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(54)
    EndAttack()
    SLOT_51 = 0
    PerInertia(10)
    XImpulseAcceleration(10)
    YAccel(10)
    PerGravity(10)
    CommonSE('006_swing_blade_0')
    sprite('mi408_f07', 2)
    sprite('mi408_f04', 4)
    sprite('mi408_f05', 4)
    sprite('mi408_f06', 4)
    sprite('mi408_f07', 1)
    sprite('null', 32)
    CreateObject('mi408_DelEff', 0)


@State
def mi408_DelEff():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        LinkParticle('mief408_del')
    sprite('null', 60)
    CreateObject('mi408_DelEffSub', -1)


@State
def mi408_DelEffSub():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        Eff3DEffect('mieff408_deleff00', '')
        E0EAEffectScale(2)
    sprite('null', 20)
    CreateObject('mi408_DelEffSub2', -1)
    sprite('null', 20)
    ConstantAlphaModifier(-12)


@State
def mi408_DelEffSub2():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        Size(2400)
        AddRotationPerFrame(15000)
    sprite('vrmi408_yugami', 30)
    ParticleTransparency(1)
    PlayerTransparency(50000)
    Unknown3059(-1000)
    SetScaleSpeed(-20)


@State
def mi408_CreateEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        ParticleLayer(11)
        CallPrivateEffect('mief408_del')
        Eff3DEffect('mieff408_deleff01', '')
        CopyFromRightToLeft(23, 2, 60, 3, 2, 60)
        if SLOT_60 == 1:
            PrivateFunction3(3, -50000, 310000, 100, 0)
        if SLOT_60 == 2:
            PrivateFunction3(3, -50000, 160000, 100, 0)
        if SLOT_60 == 3:
            PrivateFunction3(3, -50000, 210000, 100, 0)
        if not SLOT_60:
            if not SLOT_60 == 3:
                PrivateFunction3(3, -50000, 360000, 100, 0)
            else:
                PrivateFunction3(3, -50000, 210000, 100, 0)
        E0EAEffectPosition(2)
        Size(1200)
    sprite('null', 20)
    PrivateSE('mise_17')
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def FunnelTimeStopThrow():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')
        clearUponHandler(41)
        clearUponHandler(VALUE_RECEIVED)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(PLAYER_DAMAGED, 99)

        def upon_EVERY_FRAME():
            callSubroutine('Funnel_Disp')
            callSubroutine('Funnel_Pallet')

        def upon_STATE_END():
            SetScaleSpeed(0)
            Size(1000)
            AlphaValue(255)
            ConstantAlphaModifier(0)
    sprite('keep', 6)
    sprite('mi000_f00', 6)
    sprite('mi431_f00', 6)
    sprite('mi431_f01', 300)
    ConstantAlphaModifier(-8)
    label(0)
    sprite('mi431_f01', 16)
    AlphaValue(128)
    ConstantAlphaModifier(8)
    sprite('mi431_f00', 4)
    loopRest()
    gotoLabel(99)
    label(1)
    sprite('mi431_f02', 300)
    ConstantAlphaModifier(8)
    label(2)
    sprite('mi431_f03', 9)
    sprite('mi431_f04', 9)
    sprite('mi431_f05', 7)
    label(99)
    sprite('keep', 10)
    PrivateFunction2('FunnelNeutral', 100)


@State
def FunnelTimeStopThrow_Open():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')
        clearUponHandler(41)
        clearUponHandler(VALUE_RECEIVED)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(PLAYER_DAMAGED, 99)

        def upon_EVERY_FRAME():
            callSubroutine('Funnel_Disp')
            callSubroutine('Funnel_Pallet')

        def upon_STATE_END():
            SetScaleSpeed(0)
            Size(1000)
            AlphaValue(255)
            ConstantAlphaModifier(0)
    sprite('mi203_f02', 10)
    AddY(-40000)
    sprite('mi203_f01', 4)
    AddY(10000)
    sprite('mi203_f00', 4)
    AddY(10000)
    sprite('mi431_f01', 300)
    AddY(20000)
    ConstantAlphaModifier(-8)
    label(0)
    sprite('mi431_f01', 8)
    AlphaValue(128)
    ConstantAlphaModifier(8)
    sprite('mi203_f00', 4)
    sprite('mi203_f01', 4)
    sprite('mi203_f02', 4)
    loopRest()
    gotoLabel(99)
    label(1)
    sprite('mi431_f02', 300)
    ConstantAlphaModifier(8)
    label(2)
    sprite('mi431_f02', 10)
    AddY(-10000)
    sprite('mi203_f00', 5)
    AddX(30000)
    AddY(-10000)
    sprite('mi203_f01', 5)
    AddX(30000)
    AddY(-10000)
    sprite('mi203_f02', 5)
    AddX(30000)
    AddY(-10000)
    label(99)
    sprite('keep', 10)
    PrivateFunction2('FunnelNeutral_Open', 100)


@State
def FunnelMatchWin2():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')
        uponSendToLabel(32, 0)
    sprite('null', 2000)
    label(0)
    sprite('mi611_f12', 7)
    sprite('mi611_f13', 7)
    sprite('mi611_f14', 7)
    sprite('mi611_f15', 7)
    sprite('mi611_f16', 7)
    sprite('mi611_f17', 7)
    sprite('mi611_f18', 7)
    sprite('mi611_f19', 7)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('keep', 10)
    PrivateFunction2('FunnelNeutral', 100)


@State
def FunnelRoundWin():

    def upon_IMMEDIATE():
        callSubroutine('FU_ActReset')
        RenderLayer(0)
    sprite('mi615_f00', 6)
    sprite('mi615_f01', 6)
    sprite('mi615_f02', 6)
    sprite('mi615_f03', 6)
    sprite('mi615_f04', 6)
    sprite('mi615_f05', 6)
    label(1)
    sprite('mi615_f06', 7)
    sprite('mi615_f07', 7)
    sprite('mi615_f08', 7)
    sprite('mi615_f09', 7)
    sprite('mi615_f10', 7)
    sprite('mi615_f11', 7)
    sprite('mi615_f12', 7)
    sprite('mi615_f13', 7)
    loopRest()
    gotoLabel(1)
    label(99)
    sprite('keep', 10)
    PrivateFunction2('FunnelNeutral', 100)


@State
def test00sub():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RenderLayer(1)
        PaletteIndex(6)
        BlendMode_Sub()
        AddX(-128000)
    sprite('vr_test00_10', 20)
    AlphaValue(255)
    ConstantAlphaModifier(-12)
    CreateObject('test00add', -1)


@State
def test00add():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(3)
        E0EAEffectPosition(2)
        E0EAEffectRotation(2)
        IgnorePauses(2)
        RenderLayer(1)
        PaletteIndex(6)
        BlendMode_Add()
    sprite('vr_test00_00', 10)
    AlphaValue(255)
    ConstantAlphaModifier(-12)
    ConstantRedModifier(-25)
    sprite('vr_test00_00', 10)
    ConstantGreenModifier(-25)


@State
def mi202eff():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(2)
        BlendMode_Sub()
        RemoveOnCallStateEnd(3)
        AlphaValue(180)
        AddX(-100000)
        RenderLayer(1)
        Size(800)
    sprite('vrmi202_10', 2)
    CreateObject('mi202sub', -1)
    sprite('vrmi202_11', 2)
    sprite('vrmi202_12', 2)
    IgnorePauses(2)
    ConstantAlphaModifier(-30)
    sprite('vrmi202_13', 2)
    sprite('vrmi202_14', 2)


@State
def mi202sub():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(3)
        IgnorePauses(2)
        E0EAEffectRotation(2)
        RenderLayer(1)
        Size(800)
    sprite('vrmi202_00', 2)
    sprite('vrmi202_01', 2)
    sprite('vrmi202_02', 2)
    ConstantAlphaModifier(-42)
    sprite('vrmi202_03', 2)
    sprite('vrmi202_04', 2)


@State
def mi212eff():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(2)
        BlendMode_Sub()
        IgnorePauses(2)
        RemoveOnCallStateEnd(3)
        Flip()
        AddX(75000)
        AddY(140000)
        AlphaValue(180)
    sprite('vrmi212_10', 3)
    CreateObject('mi212sub', -1)
    CreateObject('mi212sub', -1)
    sprite('vrmi212_11', 4)
    AddX(100000)
    AddY(-23500)
    ConstantAlphaModifier(-35)
    sprite('vrmi212_11', 2)


@State
def mi212sub():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(3)
    sprite('vrmi212_00', 3)
    sprite('vrmi212_01', 4)
    ConstantAlphaModifier(-51)
    sprite('vrmi212_01', 2)


@State
def mi212eff2():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Sub()
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        AlphaValue(160)
        AddX(50000)
    sprite('vrmi212_14', 4)
    CreateObject('mi212sub2', -1)
    ScreenShake(8000, 8000)
    sprite('vrmi212_15', 3)
    sprite('vrmi212_16', 3)
    sprite('vrmi212_17', 3)
    SetScaleSpeed(30)
    sprite('vrmi212_18', 4)
    SetScaleSpeed(60)


@State
def mi212sub2():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(3)
    sprite('vrmi212_04', 4)
    sprite('vrmi212_05', 3)
    sprite('vrmi212_06', 3)
    sprite('vrmi212_07', 3)
    ConstantAlphaModifier(-30)
    SetScaleSpeed(20)
    sprite('vrmi212_08', 4)
    SetScaleSpeed(60)


@State
def mi232():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        IgnorePauses(2)
        AddY(150000)
        AddX(160000)
        RemoveOnCallStateEnd(2)
    sprite('vrmi232_00', 4)
    CreateObject('mi232Sub', -1)
    sprite('vrmi232_01', 3)
    sprite('vrmi232_02', 3)
    AlphaValue(200)
    sprite('vrmi232_03', 2)
    AlphaValue(175)


@State
def mi232Particle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        callSubroutine('Funnel_Pallet')
    label(0)
    sprite('null', 1)
    ParticleColorFromPalette(64, 64, 64)
    CallCustomizableParticle('mief_bitnokosi_back', -1)
    gotoLabel(0)


@State
def mi232Sub():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Sub()
        E0EAEffectScale(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        AlphaValue(150)
    sprite('vrmi232_10', 4)
    sprite('vrmi232_11', 3)
    sprite('vrmi232_12', 3)
    sprite('vrmi232_13', 2)


@State
def mi252eff():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(2)
        BlendMode_Sub()
        RemoveOnCallStateEnd(3)
        IgnorePauses(2)
        AlphaValue(180)
        AddX(-100000)
        Size(800)
    sprite('vrmi202_11', 2)
    CreateObject('mi252sub', -1)
    sprite('vrmi202_12', 2)
    AddX(10000)
    ConstantAlphaModifier(-30)
    Size(650)
    RenderLayer(2)
    sprite('vrmi202_13', 2)
    sprite('vrmi202_14', 2)


@State
def mi252sub():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(3)
        IgnorePauses(2)
        E0EAEffectRotation(2)
        Size(800)
    sprite('vrmi202_01', 2)
    sprite('vrmi202_02', 2)
    ConstantAlphaModifier(-42)
    RenderLayer(2)
    Size(650)
    sprite('vrmi202_03', 2)
    sprite('vrmi202_04', 2)


@State
def mi252Particle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        callSubroutine('Funnel_Pallet')
    label(0)
    sprite('null', 1)
    ParticleColorFromPalette(64, 64, 64)
    CallCustomizableParticle('mief_bitnokosi', -1)
    gotoLabel(0)


@State
def mi311eff():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        E0EAEffectPosition(2)
        BlendMode_Sub()
        RemoveOnCallStateEnd(3)
        IgnorePauses(2)
        AlphaValue(180)
        RenderLayer(1)
        Size(1200)
    sprite('vrmi311_10', 2)
    CreateObject('mi311sub', -1)
    sprite('vrmi311_11', 2)
    sprite('vrmi311_12', 2)
    sprite('vrmi311_13', 2)


@State
def mi311sub():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        E0EAEffectScale(2)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(3)
        IgnorePauses(2)
        E0EAEffectRotation(2)
        E0EAEffectDirection(2)
        RenderLayer(1)
    sprite('vrmi311_00', 2)
    AlphaValue(255)
    sprite('vrmi311_01', 2)
    sprite('vrmi311_02', 2)
    AlphaValue(150)
    sprite('vrmi311_03', 2)
    AlphaValue(100)


@State
def mi312():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        IgnorePauses(2)
        AddY(150000)
        AddX(-17500)
        RemoveOnCallStateEnd(2)
        Flip()
    sprite('vrmi232_01', 3)
    AlphaValue(160)
    CreateObject('mi312Sub', -1)
    sprite('vrmi232_02', 3)
    sprite('vrmi232_03', 2)
    AlphaValue(145)


@State
def mi312Sub():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Sub()
        E0EAEffectScale(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        RemoveOnCallStateEnd(2)
        AlphaValue(200)
    sprite('vrmi232_11', 3)
    sprite('vrmi232_12', 3)
    sprite('vrmi232_13', 2)


@State
def huyu():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        LinkParticle('mief_huyu')
        Size(200)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)

        def upon_EVERY_FRAME():
            if SLOT_31 <= 30:
                sendToLabel(10)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    SetScaleSpeed(75)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    SetScaleSpeed(0)
    label(0)
    sprite('null', 60)
    ConstantAlphaModifier(0)
    SetScaleSpeed(0)
    AlphaValue(255)
    Size(950)
    sprite('null', 600)
    ConstantAlphaModifier(0)
    SetScaleSpeed(0)
    label(10)
    sprite('null', 32767)
    clearUponHandler(EVERY_FRAME)
    CreateObject('mief_huyu_pinti', -1)
    AlphaValue(0)
    label(1)
    sprite('null', 5)
    TriggerUponForState('mief_huyu_pinti', 32)
    E0EAEffectPosition(0)
    SLOT_4 = 0
    ConstantAlphaModifier(-51)
    SetScaleSpeed(60)
    loopRest()


@State
def mief_huyu_pinti():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
        LinkParticle('mief_huyu_pinti')
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 10)
    AlphaValue(255)
    ConstantAlphaModifier(-20)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    AlphaValue(0)
    CreateParticle('mief_huyu_pintiEnd', -1)


@State
def mi400_effMato():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        CancelIfPlayerHit(3)
        BlendMode_Normal()
        AddX(-12500)
        uponSendToLabel(33, 1)
    sprite('null', 5)
    CreateObject('mi400_eff2', -1)
    sprite('null', 9)
    CreateObject('mi400_eff3', -1)
    sprite('null', 20)
    CreateObject('mi400_eff', -1)
    TriggerUponForState('mi400_eff3', 32)
    sprite('null', 32767)
    label(1)
    sprite('null', 1)
    ScreenShake(10000, 10000)
    TriggerUponForState('mi400_eff2', 32)
    TriggerUponForState('mi400_eff', 32)


@State
def mi400_eff():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        AttackP2(94)
        SameMoveProration(10)
        Hitstop(2)
        EnemyHitstopAddition(-1, -1, -1)
        BounceOffWall(1)
        HitBackReturnObject(1)
        Unknown9219(1)
        StarterRating(2)
        if SLOT_11:
            callSubroutine('TimeStop_Atk')
            Damage(300)
        else:
            Damage(500)
            AttackDirection(0)
            PushbackX(30400)
            AirPushbackY(38000)
            AirPushbackX(12000)
            AirUntechableTime(60)
            HardKnockdown(1)
            UseFireHitspark(1)
        BlendMode_Normal()
        Size(600)
        AlphaValue(0)
        AddY(530000)
        WallCollisionDetection(1)
        SLOT_51 = 0

        def upon_EVERY_FRAME():
            if SLOT_StateDuration == 45:
                CreateParticle('mief400_lvup', -1)
                Size(800)
                AddY(10000)
                RefreshMultihit()
                if not SLOT_11:
                    Damage(600)
                SLOT_51 = 1
                PrivateSE('mise_09')
            if SLOT_StateDuration == 75:
                CreateParticle('mief400_lvup', -1)
                Size(900)
                AddY(10000)
                RefreshMultihit()
                if not SLOT_11:
                    Damage(700)
                SLOT_51 = 2
                PrivateSE('mise_09')
            if SLOT_StateDuration == 105:
                CreateParticle('mief400_lvup', -1)
                Size(1050)
                AddY(10000)
                RefreshMultihit()
                if not SLOT_11:
                    Damage(800)
                SLOT_51 = 3
                PrivateSE('mise_09')
            if SLOT_StateDuration >= 165:
                TriggerUponForState('SpecialShot', 32)

        def upon_32():
            SetActionMark(1)
            sendToLabel(1)
        uponSendToLabel(LANDING, 2)
        ContinueState(600)
        SLOT_8 = 1

        def upon_PLAYER_DAMAGED():
            SLOT_8 = 0
            DeleteObject(23)
        CopyFromRightToLeft(23, 2, 55, 3, 2, 55)
        if not SLOT_55:
            SLOT_8 = 0
            DeleteObject(23)
    sprite('vrmi400', 5)
    ConstantAlphaModifier(40)
    AttackOff()
    CreateObject('mi400_Ball', -1)
    CreateObject('mi400_AuraRenzoku', -1)
    sprite('vrmi400', 4)
    RefreshMultihit()
    label(0)
    sprite('vrmi400', 4)
    if SLOT_11:
        RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrmi400', 4)
    E0EAEffectPosition(0)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(OPPONENT_CHAR_HIT_OR_BLOCK)
    Damage(300)
    HitBackReturnObject(0)
    Unknown9219(0)
    if not SLOT_11:
        AirPushbackY(-12000)
        PushbackX(8000)
        Floorslide(10)
    RefreshMultihit()
    if CheckInput(0x5f):
        physicsYImpulse(-15000)
        physicsXImpulse(7500)
        RotationAngle(-30000)
    else:
        if SLOT_19 >= 500000:
            SLOT_XVelocity = SLOT_XVelocity + SLOT_19
        else:
            SLOT_XVelocity = 500000
        SLOT_YVelocity = SLOT_YVelocity + SLOT_YDistanceFromFloor
        XImpulseAcceleration(1)
        YAccel(-1)
        RotationSomething(0)
        TriggerUponForState('mi400_Ball', 32)
    if SLOT_51:
        SmartVoiceline('mi201')
    sprite('vrmi400', 4)
    RefreshMultihit()
    XImpulseAcceleration(120)
    YAccel(120)
    sprite('vrmi400', 4)
    RefreshMultihit()
    XImpulseAcceleration(120)
    YAccel(120)
    sprite('vrmi400', 4)
    RefreshMultihit()
    XImpulseAcceleration(130)
    YAccel(130)
    sprite('vrmi400', 4)
    RefreshMultihit()
    XImpulseAcceleration(130)
    YAccel(130)
    label(10)
    sprite('vrmi400', 4)
    RefreshMultihit()
    if SLOT_51 <= 0:
        XImpulseAcceleration(110)
        YAccel(110)
    if SLOT_51 == 1:
        XImpulseAcceleration(107)
        YAccel(107)
    if SLOT_51 == 2:
        XImpulseAcceleration(104)
        YAccel(104)
    if SLOT_51 >= 3:
        XImpulseAcceleration(101)
        YAccel(101)
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('vrmi400', 1)
    AttackOff()
    CreateObject('mi400_tyakuti', -1)
    DespawnEAEffect('mi400_AuraRenzoku')
    DespawnEAEffect('mi400_Ball')
    AlphaValue(0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    SetScaleSpeed(120)
    ScreenShake(20000, 20000)


@State
def mi400_Ball():

    def upon_IMMEDIATE():
        BlendMode_Add()
        E0EAEffectRotation(2)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        PaletteIndex(3)
        EnableAfterimage(1)
        AfterimageCount(2)
        uponSendToLabel(32, 1)
    sprite('vrmi400_20', 1)
    CreateObject('mi400_BallSub', -1)
    label(0)
    sprite('vrmi400_20', 3)
    sprite('vrmi400_21', 3)
    sprite('vrmi400_22', 3)
    sprite('vrmi400_23', 3)
    sprite('vrmi400_24', 3)
    sprite('vrmi400_25', 3)
    gotoLabel(0)
    label(1)
    sprite('vrmi400_20', 1)
    Rotation(-90000)
    CreateObject('mi400_BallCircle', -1)
    label(2)
    sprite('vrmi400_20', 3)
    CreateObject('mi400_BallEnd', 0)
    CreateObject('mi400_BallEnd', 1)
    CreateObject('mi400_BallEnd', 2)
    CreateObject('mi400_BallEnd', 3)
    CreateObject('mi400_BallEnd', 4)
    sprite('vrmi400_21', 3)
    CreateObject('mi400_BallEnd', 0)
    CreateObject('mi400_BallEnd', 1)
    CreateObject('mi400_BallEnd', 2)
    CreateObject('mi400_BallEnd', 3)
    CreateObject('mi400_BallEnd', 4)
    sprite('vrmi400_22', 3)
    CreateObject('mi400_BallEnd', 0)
    CreateObject('mi400_BallEnd', 1)
    CreateObject('mi400_BallEnd', 2)
    CreateObject('mi400_BallEnd', 3)
    CreateObject('mi400_BallEnd', 4)
    sprite('vrmi400_23', 3)
    CreateObject('mi400_BallEnd', 0)
    CreateObject('mi400_BallEnd', 1)
    CreateObject('mi400_BallEnd', 2)
    CreateObject('mi400_BallEnd', 3)
    CreateObject('mi400_BallEnd', 4)
    sprite('vrmi400_24', 3)
    CreateObject('mi400_BallEnd', 0)
    CreateObject('mi400_BallEnd', 1)
    CreateObject('mi400_BallEnd', 2)
    CreateObject('mi400_BallEnd', 3)
    CreateObject('mi400_BallEnd', 4)
    sprite('vrmi400_25', 3)
    CreateObject('mi400_BallEnd', 0)
    CreateObject('mi400_BallEnd', 1)
    CreateObject('mi400_BallEnd', 2)
    CreateObject('mi400_BallEnd', 3)
    CreateObject('mi400_BallEnd', 4)
    gotoLabel(2)


@State
def mi400_BallSub():

    def upon_IMMEDIATE():
        BlendMode_Sub()
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        PaletteIndex(1)
        EnableAfterimage(1)
    sprite('vrmi400_30', 32767)
    Size(1200)


@State
def mi400_BallEnd():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(3)
        AlphaValue(150)
        Size(300)
        RandAddScaleY(-200, 400)
        E0EAEffectRotation(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
    sprite('vrmi400_60', 2)
    SetScaleSpeedY(40)
    sprite('vrmi400_61', 2)
    sprite('vrmi400_62', 2)
    sprite('vrmi400_63', 2)
    ConstantAlphaModifier(-25)
    sprite('vrmi400_64', 2)
    sprite('vrmi400_65', 2)


@State
def mi400_AuraRenzoku():

    def upon_IMMEDIATE():
        uponSendToLabel(32, 0)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
    label(0)
    sprite('null', 5)
    CreateObject('mi400_Aura', -1)
    gotoLabel(0)


@State
def mi400_Aura():

    def upon_IMMEDIATE():
        BlendMode_Sub()
        RenderLayer(5)
        Eff3DEffect('mieff400_aura00', '')
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        RandAddRotation(0, 360000)
        AddRotationPerFrame(60)
    sprite('null', 15)
    CreateParticle('mief400_hasshatb', -1)
    SetScaleSpeed(120)
    ConstantAlphaModifier(-17)


@State
def mi400_BallCircle():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectScale(2)
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        Eff3DEffect('mieff400_circle2', '')
        E0EAEffectRotation(2)
        E0EAEffectPosition(2)
        Rotation(-3000)
    sprite('null', 32767)


@State
def mi400_eff2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        E0EAEffectScale(2)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 15)
    CreateObject('mi400_effsub', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mi400_effsub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(3)
        RemoveOnCallStateEnd(3)
        LinkParticle('mief400_tb')
        Eff3DEffect('mieff400_aura02', '')
        RemoveOnCallStateEnd(2)
    sprite('null', 30)
    AddScaleX(300)
    AddScaleZ(300)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def mi400_eff3():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AddY(550000)
        LinkParticle('mief404_blackball')
        RemoveOnCallStateEnd(2)
        CancelIfPlayerHit(3)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        uponSendToLabel(32, 1)
    sprite('null', 32767)
    SetScaleSpeed(15)
    label(1)
    sprite('null', 5)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mi400_tyakuti():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        AttackP2(94)
        Damage(500)
        SameMoveProration(10)
        Hitstop(0)
        Blockstun(28)
        CHStateIfCHStart(2)
        VoodooDamageMultiplier(2)
        StarterRating(2)
        if SLOT_11:
            callSubroutine('TimeStop_Atk')
        else:
            GroundedHitstunAnimation(18)
            AirHitstunAnimation(18)
            AirPushbackY(36000)
            AirPushbackX(0)
            AirUntechableTime(60)
            UseFireHitspark(1)
        BlendMode_Sub()
        PaletteIndex(1)
        AddY(-20000)
        AlphaValue(200)

        def upon_PLAYER_DAMAGED():
            DeleteObject(23)
        CopyFromRightToLeft(23, 2, 51, 2, 2, 51)
        if SLOT_51 == 1:
            SetScaleY(1000)
            SetActionMark(1)
        if SLOT_51 == 2:
            SetScaleY(1200)
            SetActionMark(2)
        if SLOT_51 >= 3:
            SetScaleY(1400)
            SetActionMark(3)
        SLOT_8 = 1

        def upon_STATE_END():
            SLOT_8 = 0
    sprite('vrmi400_50', 5)
    CreateObject('mi400_tyakutiSub', -1)
    CommonSE('016_explode_2')
    sprite('vrmi400_51', 5)
    label(0)
    sprite('vrmi400_52', 3)
    if SLOT_2:
        RefreshMultihit()
        AddActionMark(-1)
    sprite('vrmi400_53', 3)
    if SLOT_2:
        RefreshMultihit()
        AddActionMark(-1)
    sprite('vrmi400_54', 3)
    if SLOT_2:
        RefreshMultihit()
        AddActionMark(-1)
    sprite('vrmi400_55', 3)
    if SLOT_2:
        RefreshMultihit()
        AddActionMark(-1)
    sprite('vrmi400_52', 3)
    TriggerUponForState('mi400_tyakutiSub', 32)
    ConstantAlphaModifier(-13)
    CreateObject('mi400_End', 0)
    CreateObject('mi400_End2', 1)
    CreateObject('mi400_End', 2)
    CreateObject('mi400_End2', 3)
    CreateObject('mi400_End', 4)
    CreateObject('mi400_End2', 5)
    CreateObject('mi400_End', 6)
    CreateObject('mi400_End2', 7)
    CreateObject('mi400_End', 8)
    CreateObject('mi400_End2', 9)
    CreateObject('mi400_End', 10)
    CreateObject('mi400_End2', 11)
    CreateObject('mi400_End', 12)
    sprite('vrmi400_53', 3)
    sprite('vrmi400_54', 3)
    sprite('vrmi400_55', 3)
    sprite('null', 15)
    loopRest()
    SLOT_8 = 0


@State
def mi400_tyakutiSub():

    def upon_IMMEDIATE():
        BlendMode_Add()
        LinkParticle('mief400_firejizoku')
        PaletteIndex(3)
        E0EAEffectScale(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        IgnorePauses(2)
        EnableAfterimage(1)
        AfterimageCount(3)
        uponSendToLabel(32, 1)
    sprite('vrmi400_40', 5)
    CreateObject('mi400_tyakutiSub2', -1)
    sprite('vrmi400_41', 5)
    label(0)
    sprite('vrmi400_42', 3)
    sprite('vrmi400_43', 3)
    sprite('vrmi400_44', 3)
    sprite('vrmi400_45', 3)
    gotoLabel(0)
    label(1)
    sprite('vrmi400_42', 3)
    TriggerUponForState('mi400_tyakutiSub2', 32)
    ConstantAlphaModifier(-21)
    sprite('vrmi400_43', 3)
    sprite('vrmi400_44', 3)
    sprite('vrmi400_45', 3)


@State
def mi400_tyakutiSub2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectScale(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('mieff400_aura03', '')
        AlphaValue(0)
        uponSendToLabel(32, 1)
    sprite('null', 10)
    sprite('null', 1)
    ConstantAlphaModifier(26)
    label(0)
    sprite('null', 3)
    CreateObject('mi400_tyakutiSub3', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    SetScaleSpeedY(500)
    ConstantAlphaModifier(-26)
    loopRest()


@State
def mi400_tyakutiSub3():

    def upon_IMMEDIATE():
        BlendMode_Add()
        Size(1350)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('mieff400_circle', '')
        RemoveOnContact(2)
        EnableAfterimage(1)
    sprite('null', 5)
    ConstantAlphaModifier(-4)
    physicsYImpulse(8750)
    sprite('null', 10)
    physicsYImpulse(30000)
    SetScaleSpeed(-40)
    sprite('null', 10)


@State
def mi400_HitEffect():

    def upon_IMMEDIATE():
        DespawnEAEffect('mi400_HitEffect')
        ContinueState(90)
    label(0)
    sprite('null', 6)
    CreateObject('mi400_HitEffect2', -1)
    loopRest()
    gotoLabel(0)


@State
def mi400_HitEffect2():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        BlendMode_Add()
        PaletteIndex(3)
        AlphaValue(255)
        SetScaleX(500)
        SetScaleY(225)
        EffectPosition(22, 105)
    sprite('vrmi400_60', 3)
    SetScaleSpeedY(25)
    sprite('vrmi400_61', 3)
    sprite('vrmi400_62', 3)
    sprite('vrmi400_63', 3)
    ConstantAlphaModifier(-21)
    CreateParticle('mief400_endtb', -1)
    sprite('vrmi400_64', 3)
    sprite('vrmi400_65', 3)


@State
def mi400_End():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(3)
        AlphaValue(255)
        Size(500)
        RandAddScaleY(-550, 200)
        LinkParticle('mief400_endsub')
    sprite('vrmi400_60', 6)
    SetScaleSpeedY(40)
    sprite('vrmi400_61', 4)
    sprite('vrmi400_62', 4)
    sprite('vrmi400_63', 4)
    ConstantAlphaModifier(-21)
    CreateParticle('mief400_endtb', -1)
    sprite('vrmi400_64', 4)
    sprite('vrmi400_65', 4)


@State
def mi400_End2():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(3)
        AlphaValue(255)
        Size(500)
        Flip()
        RandAddScaleY(-550, 200)
        LinkParticle('mief400_endsub')
    sprite('vrmi400_60', 6)
    SetScaleSpeedY(40)
    sprite('vrmi400_61', 5)
    sprite('vrmi400_62', 5)
    sprite('vrmi400_63', 5)
    ConstantAlphaModifier(-17)
    CreateParticle('mief400_endtb', -1)
    sprite('vrmi400_64', 5)
    sprite('vrmi400_65', 5)


@State
def mi402_eff():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        E0EAEffectPosition(3)
        IgnorePauses(2)
        AttackLevel_(4)
        Damage(800)
        AttackP2(82)
        SameMoveProration(10)
        Unknown9219(1)
        if SLOT_11:
            callSubroutine('TimeStop_Atk')
        else:
            AirUntechableTime(33)
            AirPushbackX(22000)
            AirPushbackY(23000)
            CHGroundedHitstunAnimation(2)
            CHCrumple(35)
        PaletteIndex(1)
        Size(850)
        AddX(100000)
        AddY(-10000)
        AlphaValue(220)
        WallCollisionDetection(1)

        def upon_PLAYER_DAMAGED():
            DeleteObject(23)

        def upon_56():
            E0EAEffectPosition(0)
            IgnorePauses(0)
    sprite('null', 9)
    CreateObject('mi402_eff2', -1)

    def RunOnObject_1():
        SetScaleX(-800)
        SetScaleY(800)
        AddY(30000)
        AddX(-140000)
    CreateObject('mi402_eff2', -1)
    sprite('vrmi402_00', 4)
    CreateObject('mi402_effpoint', -1)
    ParticleSize(850)
    CallCustomizableParticle('mief402_skullwave', -1)
    TriggerUponForState('mi402_eff2', 32)
    physicsXImpulse(20000)
    ScreenShake(10000, 10000)
    sprite('vrmi402_01', 4)
    XImpulseAcceleration(70)
    sprite('vrmi402_02', 4)
    XImpulseAcceleration(70)
    sprite('vrmi402_03', 2)
    physicsXImpulse(0)
    IgnorePauses(0)
    sprite('vrmi402_04', 2)
    sprite('vrmi402_04', 10)
    ConstantAlphaModifier(-51)
    CreateObject('mi402_EndEff', -1)


@State
def mi402_EndEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Flip()
        SetScaleX(570)
        SetScaleY(900)
        AddY(-35000)
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        Eff3DEffect('mieff402_end00', '')
    sprite('null', 5)
    AlphaValue(128)
    ConstantAlphaModifier(26)
    sprite('null', 8)
    SetScaleXPerFrame(1)
    SetScaleSpeedY(3)
    ConstantAlphaModifier(-5)
    CreateObject('mi402_AuraEff', -1)
    sprite('null', 5)
    Eff3DEffect('mieff402_end01', '')
    sprite('null', 11)


@State
def mi402_AuraEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Flip()
        SetScaleX(570)
        SetScaleY(800)
        Eff3DEffect('mieff402_aura00', '')
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    sprite('null', 13)
    SetScaleSpeedY(7)
    CreateObject('mi402_gsand', -1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mi402_gsand():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('mief402_gsand')
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        AddY(80000)
    sprite('null', 10)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mi401_shockMato():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        PaletteIndex(1)
        AddX(200000)
        AddY(200000)
    label(0)
    sprite('null', 4)
    CreateObject('mi401_shock', -1)
    gotoLabel(0)


@State
def mi401_shock():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        Flip()
        AlphaValue(130)
        Size(500)
        EnableAfterimage(1)
    sprite('vrmi401_00', 4)
    SetScaleSpeed(200)
    sprite('vrmi401_01', 3)
    SetScaleSpeed(100)
    sprite('vrmi401_02', 2)
    ConstantAlphaModifier(-28)
    SetScaleSpeed(50)
    sprite('vrmi401_03', 2)
    sprite('vrmi401_04', 2)


@State
def mi401_shotei2():

    def upon_IMMEDIATE():
        BlendMode_Sub()
        PaletteIndex(1)
        AddY(200000)
        AddX(150000)
        SetScaleX(1400)
        SetScaleY(600)
        AlphaValue(200)
        RenderLayer(2)
    sprite('vrmi401_22', 6)
    CreateObject('mi401_shoteiAdd2', -1)
    sprite('vrmi401_23', 2)
    ConstantAlphaModifier(-25)
    sprite('vrmi401_24', 2)
    sprite('vrmi401_25', 2)
    sprite('vrmi401_26', 2)


@State
def mi401_shoteiAdd2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectScale(2)
        RemoveOnContact(2)
        BlendMode_Add()
        PaletteIndex(1)
    sprite('vrmi401_12', 6)
    sprite('vrmi401_13', 2)
    sprite('vrmi401_14', 2)
    sprite('vrmi401_15', 2)
    sprite('vrmi401_16', 2)


@State
def mi401_shotei():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(1)
        Flip()
        TeleportToObject(22)
        AddY(200000)
        AddX(-150000)
        RenderLayer(2)
        Size(1500)
        AlphaValue(200)
    sprite('vrmi401_20', 2)
    CreateObject('mi401_shoteiAdd', -1)
    CreateObject('mi401_shock', -1)
    CreateParticle('mief401_speeds', -1)
    sprite('vrmi401_21', 6)
    ConstantAlphaModifier(-11)
    sprite('vrmi401_22', 6)
    CreateParticle('mief401_tb', 0)
    CreateParticle('mief401_tb2', 1)
    ParticleLayer(11)
    CallCustomizableParticle('mief401_bst', 2)
    sprite('vrmi401_23', 2)


@State
def mi401_shoteiAdd():

    def upon_IMMEDIATE():
        BlendMode_Add()
        PaletteIndex(1)
        RenderLayer(2)
        Size(1500)
        AlphaValue(125)
    sprite('vrmi401_10', 2)
    sprite('vrmi401_11', 6)
    sprite('vrmi401_12', 6)
    sprite('vrmi401_13', 2)


@State
def mi401_Gedan():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Sub()
        PaletteIndex(1)
        AddX(250000)
        AddY(-10000)
        Size(1600)
        AlphaValue(160)
        CreateObject('mi401_GendanAdd', -1)
        RenderLayer(11)
    label(0)
    sprite('vrmi401_40', 2)
    CreateParticle('mief401_gedan', -1)
    sprite('vrmi401_41', 2)
    sprite('vrmi401_42', 2)
    CreateParticle('mief401_gedan', -1)
    sprite('vrmi401_43', 2)
    gotoLabel(0)


@State
def mi401_GendanAdd():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectScale(2)
        BlendMode_Add()
        PaletteIndex(1)
        AlphaValue(125)
        RenderLayer(11)
    label(0)
    sprite('vrmi401_30', 2)
    sprite('vrmi401_31', 2)
    sprite('vrmi401_32', 2)
    sprite('vrmi401_33', 2)
    gotoLabel(0)


@State
def mi401_Gedan2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        BlendMode_Sub()
        PaletteIndex(1)
        AddY(-20000)
        Size(1500)
        AlphaValue(160)
        CreateObject('mi401_GendanAdd2', -1)
        RenderLayer(6)
    label(0)
    sprite('vrmi401_42', 2)
    CreateObject('mi401_Nokosi', -1)
    sprite('vrmi401_43', 2)
    CreateObject('mi401_Nokosi', -1)
    sprite('vrmi401_40', 2)
    sprite('vrmi401_41', 2)
    gotoLabel(0)


@State
def mi401_GendanAdd2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectScale(2)
        BlendMode_Add()
        PaletteIndex(1)
        RenderLayer(6)
        AlphaValue(125)
    label(0)
    sprite('vrmi401_32', 2)
    sprite('vrmi401_33', 2)
    sprite('vrmi401_30', 2)
    sprite('vrmi401_31', 2)
    gotoLabel(0)


@State
def mi401_Nokosi():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AddX(-135000)
        Size(800)
        AlphaValue(160)
        Eff3DEffect('mieff430_smoke00', '')
    sprite('null', 11)
    physicsXImpulse(-4000)
    SetScaleSpeed(40)
    sprite('null', 12)
    ConstantAlphaModifier(-13)


@State
def mi402_eff2():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        LinkParticle('mief402_skull')
        uponSendToLabel(32, 0)
        AlphaValue(0)
    sprite('null', 10)
    ConstantAlphaModifier(17)
    sprite('null', 32767)
    ConstantAlphaModifier(0)
    label(0)
    sprite('null', 1)
    AlphaValue(0)
    CreateParticle('mief402_skullfly_ippai', -1)
    loopRest()


@State
def mi402_effpoint():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        IgnorePauses(2)
        Visibility(1)
        Size(800)
        AddX(-170000)
    sprite('vrmi402_expoint', 7)
    CreateParticle('mief402_end_aura', 0)
    sprite('vrmi402_expoint', 3)
    CreateParticle('mief402_end_aura', 1)
    sprite('vrmi402_expoint', 3)
    CreateParticle('mief402_end_aura', 2)
    sprite('vrmi402_expoint', 3)
    CreateParticle('mief402_end_aura', 3)
    sprite('vrmi402_expoint', 3)
    CreateParticle('mief402_end_aura', 4)


@State
def mi403Eff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        Size(1300)
        AddY(130000)
        AddX(5000)
        AddScaleX(100)
        Visibility(1)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(0)
    sprite('null', 32767)
    Eff3DEffect('mieff403_skull_jizoku', '')
    ScreenShake(6000, 6000)
    AlphaValue(0)
    ConstantAlphaModifier(51)
    label(0)
    sprite('null', 1)
    IgnoreFinishStop(1)
    IgnoreScreenfreeze(1)
    CreateObject('mi403EffEnd', -1)


@State
def mi403EffEnd():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(1300)
        AddScaleX(100)
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
    sprite('null', 7)
    CreateObject('mi403EffParticle', -1)
    Eff3DEffect('mieff403_skull_end', '')
    SetScaleXPerFrame(20)
    SetScaleSpeedY(7)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def mi403EffParticle():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        BlendMode_Normal()
        Size(1000)
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        Visibility(1)
    label(0)
    sprite('vrmi403_particlepos', 7)
    CreateParticle('mief403_aura', 0)
    CreateParticle('mief403_aura', 1)
    CreateParticle('mief403_aura', 3)
    gotoLabel(0)


@State
def mi404_eff():

    def upon_IMMEDIATE():

        def upon_16():
            PrivateFunction3(3, -1250, -125000, 100, 1)
        E0EAEffectDirection(2)
        E0EAEffectObjectZ(2)
        RemoveOnContact(3)
        PaletteIndex(1)
        Size(900)
        AlphaValue(160)
        SLOT_6 = 600
        SetActionMark(1)

        def upon_EVERY_FRAME():
            if not SLOT_6:
                sendToLabel(1)
            if SLOT_6 <= 0:
                sendToLabel(1)

        def upon_PLAYER_DAMAGED():
            sendToLabel(1)
    sprite('vrmi404_03', 27)
    CreateObject('mi404_effStart', -1)
    CreateObject('mi404_effImp', -1)
    label(0)
    sprite('vrmi404_00', 5)
    AlphaValue(120)
    ConstantAlphaModifier(-4)
    physicsYImpulse(600)
    CreateParticle('mief404_jizoku', 0)
    sprite('vrmi404_00', 5)
    CreateParticle('mief404_jizoku', 1)
    sprite('vrmi404_00', 5)
    CreateParticle('mief404_jizoku', 2)
    sprite('vrmi404_00', 5)
    CreateParticle('mief404_jizoku', 3)
    sprite('vrmi404_00', 5)
    ConstantAlphaModifier(4)
    physicsYImpulse(-600)
    CreateParticle('mief404_jizoku', 4)
    sprite('vrmi404_00', 5)
    CreateParticle('mief404_jizoku', 5)
    sprite('vrmi404_00', 5)
    CreateParticle('mief404_jizoku', 6)
    sprite('vrmi404_00', 5)
    CreateParticle('mief404_jizoku', 7)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('vrmi404_00', 5)
    SetActionMark(0)
    AlphaValue(80)
    ConstantAlphaModifier(-10)
    YAccel(-100)
    CreateParticle('mief404_jizoku', 0)
    sprite('vrmi404_00', 5)
    ConstantAlphaModifier(10)
    CreateParticle('mief404_jizoku', 1)
    sprite('vrmi404_00', 5)
    ConstantAlphaModifier(-10)
    YAccel(-100)
    CreateParticle('mief404_jizoku', 2)
    sprite('vrmi404_00', 5)
    ConstantAlphaModifier(10)
    CreateParticle('mief404_jizoku', 3)
    sprite('vrmi404_00', 5)
    ConstantAlphaModifier(-10)
    YAccel(-100)
    CreateParticle('mief404_jizoku', 4)
    sprite('vrmi404_00', 5)
    ConstantAlphaModifier(10)
    CreateParticle('mief404_jizoku', 5)
    sprite('vrmi404_00', 5)
    ConstantAlphaModifier(-10)
    YAccel(-100)
    CreateParticle('mief404_jizoku', 6)
    sprite('vrmi404_00', 5)
    ConstantAlphaModifier(10)
    CreateParticle('mief404_jizoku', 7)
    sprite('vrmi404_00', 5)
    ConstantAlphaModifier(-10)
    YAccel(-100)
    CreateParticle('mief404_jizoku', 0)
    loopRest()
    gotoLabel(2)
    label(1)
    sprite('vrmi404_01', 1)
    SLOT_6 = 0
    clearUponHandler(16)
    clearUponHandler(EVERY_FRAME)
    clearUponHandler(33)
    clearUponHandler(PLAYER_DAMAGED)
    clearUponHandler(STATE_END)
    SLOT_6 = 0
    IgnoreFinishStop(1)
    IgnoreScreenfreeze(1)
    AlphaValue(128)
    ConstantAlphaModifier(-10)
    sprite('vrmi404_01', 5)
    RemoveOnCallStateEnd(3)
    sprite('vrmi404_02', 6)


@State
def mi404_effStart():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        PaletteIndex(0)
        ParticleColorFromPalette(21, 21, 21)
        CallPrivateEffect('mief404_openbaria')
        Size(1100)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
        AddY(175000)
    sprite('null', 40)
    SetScaleSpeed(10)
    sprite('null', 15)
    SetScaleSpeed(40)


@State
def mi404_effEnd():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
    sprite('null', 4)
    CreateObject('mi404_endaura', -1)

    def RunOnObject_1():
        AddY(100000)
    sprite('null', 4)
    sprite('null', 12)
    CreateObject('mi404_endaura', -1)
    sprite('null', 3)
    CreateObject('mi404_endaura2', -1)


@State
def mi404_effImp():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        E0EAEffectDirection(2)
        E0EAEffectObjectZ(2)
        PaletteIndex(1)
        AlphaValue(128)
        BlendMode_Add()
    sprite('vrmi404_03', 15)
    SetScaleSpeed(52)
    physicsYImpulse(-8000)
    ConstantAlphaModifier(-13)


@State
def mi404_effImp2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(120)
        Eff3DEffect('mieff404_aura01', '')
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(3)
        Size(1200)
        AddY(150000)
    sprite('null', 10)
    SetScaleSpeed(30)
    sprite('null', 20)
    ConstantAlphaModifier(-13)


@State
def mi404_endaura():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff404_aura00', '')
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(3)
        AlphaValue(0)
        SetScaleY(800)
        SetScaleX(1100)
        SetScaleZ(1100)
    sprite('null', 5)
    ConstantAlphaModifier(51)
    sprite('null', 25)
    SetScaleXPerFrame(-2)
    SetScaleSpeedZ(-2)
    physicsYImpulse(-1500)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mi404_endaura2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff404_aura00', '')
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(3)
        SetScaleY(800)
        SetScaleX(1100)
        SetScaleZ(1100)
        AlphaValue(0)
    sprite('null', 5)
    ConstantAlphaModifier(51)
    sprite('null', 5)
    SetScaleXPerFrame(-2)
    SetScaleSpeedZ(-2)
    physicsYImpulse(-1500)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mi406_Kyuketu():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        AddY(125000)
        AddX(156250)
        AlphaValue(100)
        Rotation(17000)
        Size(900)
        EnableAfterimage(1)
        AfterimageCount(3)
    sprite('mief406_00', 6)
    ScreenShake(8000, 8000)
    CreateObject('mi406_KyuketuSub', -1)
    RenderLayer(0)
    sprite('mief406_01', 3)
    sprite('mief406_02', 3)
    sprite('mief406_03', 3)
    physicsXImpulse(-1500)
    physicsYImpulse(2000)
    sprite('mief406_04', 3)
    sprite('mief406_05', 3)
    sprite('mief406_06', 3)
    setGravity(1000)
    physicsXImpulse(-1500)
    sprite('mief406_07', 7)
    ConstantAlphaModifier(-25)


@State
def mi406_KyuketuSub():

    def upon_IMMEDIATE():
        E0EAEffectScale(2)
        E0EAEffectRotation(2)
        PaletteIndex(1)
        BlendMode_Sub()
        AlphaValue(100)
        IgnoreScreenfreeze(1)
        E0EAEffectPosition(2)
    sprite('mief406_10', 6)
    sprite('mief406_11', 3)
    sprite('mief406_12', 3)
    sprite('mief406_13', 3)
    sprite('mief406_14', 3)
    sprite('mief406_15', 3)
    sprite('mief406_16', 3)
    sprite('mief406_17', 7)


@State
def mi407_effStart():

    def upon_IMMEDIATE():
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
    sprite('mi407_fbeam01', 3)
    sprite('mi407_fbeam02', 3)
    sprite('mi407_fbeam03', 3)
    sprite('mi407_fbeam04', 2)
    sprite('mi407_fbeam05', 2)


@State
def mi431_KyushuSoul():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        IgnoreScreenfreeze(1)
        AddScale(75)
    sprite('mief430_00', 4)
    ScreenShake(10000, 10000)
    CreateParticle('mief431_aura', 0)
    sprite('mief430_01', 4)
    CreateParticle('mief431_aura', 0)
    CreateParticle('mief431_aura', 1)
    sprite('mief430_02', 8)
    CreateParticle('mief431_aura', 0)
    CreateParticle('mief431_aura', 1)
    CreateParticle('mief431_aura', 2)
    sprite('mief430_03', 8)
    CreateParticle('mief431_aura', 0)
    CreateParticle('mief431_aura', 1)
    sprite('mief430_04', 6)
    CreateParticle('mief431_aura', 0)
    CreateParticle('mief431_aura', 1)
    CreateParticle('mief431_aura', 2)
    sprite('mief430_05', 6)
    CreateParticle('mief431_aura', 0)
    CreateParticle('mief431_aura', 1)
    CreateParticle('mief431_aura', 2)
    sprite('mief430_06', 4)
    CreateParticle('mief431_aura', 0)
    CreateParticle('mief431_aura', 1)
    CreateParticle('mief431_aura', 2)
    CreateParticle('mief431_aura', 3)
    CreateParticle('mief431_aura', 4)
    CreateParticle('mief431_aura', 5)
    sprite('mief430_07', 8)
    AddX(-80000)
    AddY(-15000)
    E0EAEffectPosition(2)
    CreateParticle('mief431_aura', 0)
    CreateParticle('mief431_aura', 1)
    CreateParticle('mief431_aura', 2)
    CreateParticle('mief431_aura', 3)
    CreateParticle('mief431_aura', 4)
    sprite('mief430_08', 6)
    CreateParticle('mief431_aura', 0)
    CreateParticle('mief431_aura', 1)
    CreateParticle('mief431_aura', 2)
    CreateParticle('mief431_aura', 3)
    CreateParticle('mief431_aura', 4)
    sprite('mief430_09', 6)
    CreateParticle('mief431_aura', 0)
    CreateParticle('mief431_aura', 1)
    CreateParticle('mief431_aura', 2)
    CreateParticle('mief431_aura', 3)
    CreateParticle('mief431_aura', 4)
    sprite('mief430_10', 6)
    CreateParticle('mief431_aura', 0)
    CreateParticle('mief431_aura', 1)
    CreateParticle('mief431_aura', 2)
    CreateParticle('mief431_aura', 3)
    CreateParticle('mief431_aura', 4)
    sprite('mief430_11', 5)
    CreateParticle('mief431_aura', 0)
    CreateParticle('mief431_aura', 1)
    CreateParticle('mief431_aura', 2)
    CreateParticle('mief431_aura', 3)
    sprite('mief430_12', 4)
    CreateParticle('mief431_aura', 0)
    CreateParticle('mief431_aura', 1)


@State
def mi430_KickEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        Eff3DEffect('mieff430_kick00', '')
        Size(800)
        AddY(150000)
        AddX(45000)
        AlphaValue(200)
    sprite('null', 10)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mi430_HitEff():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff430_hiteff00', '')
        TeleportToObject(22)
        AddY(180000)
        Size(1600)
    sprite('null', 12)
    CreateParticle('mief430_hitcircle', -1)
    CreateParticle('mief430_himatu', -1)
    CreateObject('mi430_HitEffBG', -1)
    sprite('null', 5)
    ConstantAlphaModifier(-51)
    SetScaleSpeed(120)


@State
def mi430_HitEffBG():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff430_hiteff01', '')
        Size(500)
    sprite('null', 33)


@State
def mi430_HitEff2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff430_hiteff02', '')
        TeleportToObject(22)
        AddY(180000)
        Size(2000)
        AddX(100000)
        AddY(-100000)
        Rotation(10000)
    sprite('null', 16)
    ScreenShake(20000, 20000)
    CreateParticle('mief430_himatu', -1)
    CreateObject('mi430_HitEffBG', -1)


@State
def mi430_Smoke():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff430_smoke00', '')
        Size(1450)
        AlphaValue(200)
    sprite('null', 15)
    CreateParticle('mief430_speeds', -1)
    ScreenShake(7000, 7000)
    SetScaleSpeed(80)
    physicsXImpulse(-20000)
    sprite('null', 10)
    ConstantAlphaModifier(-20)


@State
def mi430_Sand():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff430_sand00', '')
        AddX(-20000)
        Size(920)
    sprite('null', 5)
    CreateParticle('mief430_sand00', -1)
    AlphaValue(0)
    ConstantAlphaModifier(51)

    def RunOnObject_3():
        ConstantAlphaModifier(-51)
    sprite('null', 7)

    def RunOnObject_3():
        ConstantAlphaModifier(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mi430_Sand2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff430_sand01', '')
        AddX(245000)
        AddY(16000)
        Size(920)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(51)

    def RunOnObject_3():
        ConstantAlphaModifier(-51)
    sprite('null', 5)

    def RunOnObject_3():
        ConstantAlphaModifier(0)
    sprite('null', 10)


@State
def mi430_Sand3():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff430_sand02', '')
        AddX(-12000)
        AddY(140000)
        Size(840)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(51)

    def RunOnObject_3():
        ConstantAlphaModifier(-51)
    sprite('null', 5)

    def RunOnObject_3():
        ConstantAlphaModifier(0)
    sprite('null', 10)


@State
def mi430_Sand4():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff430_sand03', '')
        AddX(-12500)
        AddY(0)
        Size(840)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(51)

    def RunOnObject_3():
        ConstantAlphaModifier(-51)
    sprite('null', 5)

    def RunOnObject_3():
        ConstantAlphaModifier(0)
    sprite('null', 10)


@State
def mi430_Sand5():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff430_sand04', '')
        AddX(-60000)
        AddY(140000)
        Size(840)
    sprite('null', 5)
    AlphaValue(0)
    ConstantAlphaModifier(51)

    def RunOnObject_3():
        ConstantAlphaModifier(-51)
    sprite('null', 5)

    def RunOnObject_3():
        ConstantAlphaModifier(0)
    sprite('null', 20)
    ConstantAlphaModifier(-26)


@State
def mi432_HitEffBG():

    def upon_IMMEDIATE():
        BlendMode_Sub()
        Eff3DEffect('mieff432_nigiyakasi', '')
        Size(300)
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
    sprite('null', 15)
    AlphaValue(0)
    sprite('null', 10)
    SetScaleXPerFrame(40)
    ConstantAlphaModifier(8)
    sprite('null', 10)
    SetScaleXPerFrame(20)
    ConstantAlphaModifier(0)


@State
def mi432_Tame():

    def upon_IMMEDIATE():
        LinkParticle('mief432_tame')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddY(250000)
        Size(850)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 5)
    SetScaleSpeed(-4)
    ScreenShake(1500, 1500)
    CreateObject('mi432_TameSub', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def mi432_TameSub():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        Size(1400)
        AddRotationPerFrame(15000)
    sprite('vrmi432_yugami', 10)
    SetScaleSpeed(30)
    ParticleTransparency(1)
    PlayerTransparency(62500)
    Unknown3059(-1500)
    SetScaleSpeed(-60)


@State
def mi432_Kaiho():

    def upon_IMMEDIATE():
        LinkParticle('mief432_kaiho')
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddY(250000)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 15)
    CreateObject('mi432_KaihoSub', -1)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mi432_KaihoSub():

    def upon_IMMEDIATE():
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        Size(500)
        AddRotationPerFrame(15000)
    sprite('vrmi432_yugami', 10)
    SetScaleSpeed(30)
    ParticleTransparency(1)
    PlayerTransparency(250000)
    Unknown3059(-6000)
    sprite('vrmi432_yugami', 30)
    SetScaleSpeed(120)


@State
def TimeStopFinish():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        Damage(100)
        MinimumDamage(100)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(2)
        Stagger(30)
        Crumple(999)
        PushbackX(60000)
        AirHitstunAnimation(12)
        AirPushbackX(100000)
        AirPushbackY(1000)
        YImpulseBeforeWallbounce(0)
        WallbounceReboundTime(0)
        AirUntechableTime(999)
        Hitstop(1)
        HitsparkSize(0)
        OnlyHitPlayer(1)
        PassByArmor(1)
        DamageEffect(8, '')
        HitAnywhere(1)
        AutoHitSignalSending(0)
        AttackDirection(1)
        CopyFromRightToLeft(23, 2, 2, 22, 2, 38)
        if SLOT_IsFacingRight == SLOT_2:
            FlipOnHit(1)
        Visibility(1)
        SLOT_11 = 0
    sprite('vrmi400', 1)
    PrivateSE('mise_14')


@State
def mi440_juso():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        TeleportToObject(22)
        uponSendToLabel(32, 1)
    sprite('null', 2)
    CreateObject('mi440_jusoFire', -1)

    def RunOnObject_1():
        AddY(350000)
        AddX(105000)
    CommonSE('016_explode_1')
    CommonSE('016_explode_1')
    CreateObject('mi440_jusoSub', -1)

    def RunOnObject_1():
        AddY(350000)
        RotationAngle(12000)
    sprite('null', 2)
    CreateObject('mi440_jusoFire', -1)

    def RunOnObject_1():
        AddY(300000)
        AddX(-130000)
    sprite('null', 2)
    CreateObject('mi440_jusoSub', -1)

    def RunOnObject_1():
        AddY(250000)
        RotationAngle(10000)
        AddScale(-200)
    CreateObject('mi440_jusoFire', -1)

    def RunOnObject_1():
        AddY(160000)
    sprite('null', 2)
    CreateObject('mi440_jusoFire', -1)

    def RunOnObject_1():
        AddY(200000)
        AddX(200000)
    sprite('null', 2)
    CreateObject('mi440_jusoSub', -1)

    def RunOnObject_1():
        AddY(120000)
        AddX(2000)
        RotationAngle(10000)
    CreateObject('mi440_jusoFire', -1)

    def RunOnObject_1():
        AddY(25000)
        AddX(-120000)
        AddScale(100)
    CreateObject('mi440_jusoFireBG', -1)
    sprite('null', 2)
    CreateObject('mi440_jusoFire', -1)

    def RunOnObject_1():
        AddY(60000)
        AddX(120000)
    CreateObject('mi440_jusoFireG', -1)

    def RunOnObject_1():
        AddScale(100)
        AddScaleY(200)
    CommonSE('015_blaze_2')
    CommonSE('015_blaze_2')
    sprite('null', 32767)
    label(1)
    sprite('null', 5)
    TriggerUponForState('mi440_jusoFire', 32)
    CommonSE('016_explode_0')
    CommonSE('016_explode_0')
    sprite('null', 20)
    TriggerUponForState('mi440_jusoFireBG', 32)
    TriggerUponForState('mi440_jusoFireG', 32)
    TriggerUponForState('mi440_jusoSub', 32)
    CommonSE('016_explode_0')
    CommonSE('015_blaze_2')
    sprite('null', 32767)
    TriggerUponForState('mi440_jusoSub', 33)


@State
def mi440_jusoSub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        LinkParticle('mief440_moji')
        PaletteIndex(1)
        ColorFromPaletteIndex(120)
        Size(1000)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
    sprite('null', 15)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    label(1)
    sprite('null', 5)
    SetScaleSpeed(45)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    loopRest()


@State
def mi440_jusoFire():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('mieff440_jusoFire00', '')
        Size(750)
        AlphaValue(0)
        uponSendToLabel(32, 1)
    sprite('null', 15)
    ConstantAlphaModifier(9)
    label(0)
    sprite('null', 20)
    physicsYImpulse(375)
    ConstantAlphaModifier(0)
    SetScaleSpeedY(-5)
    sprite('null', 20)
    SetScaleSpeedY(5)
    sprite('null', 5)
    physicsYImpulse(187)
    sprite('null', 20)
    physicsYImpulse(-187)
    SetScaleSpeedY(5)
    sprite('null', 20)
    SetScaleSpeedY(-5)
    sprite('null', 5)
    physicsYImpulse(-187)
    gotoLabel(0)
    label(1)
    sprite('null', 20)
    SetScaleSpeedY(100)
    SetScaleXPerFrame(50)
    sprite('null', 20)
    ConstantAlphaModifier(-13)
    loopRest()


@State
def mi440_jusoFireG():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        LinkParticle('mief440_grondadd')
        Eff3DEffect('mieff440_jusoFire01', '')
        Size(750)
        SetScaleY(150)
        AlphaValue(0)
        uponSendToLabel(32, 1)
    sprite('null', 15)
    ConstantAlphaModifier(13)
    SetScaleSpeedY(25)
    label(0)
    sprite('null', 20)
    SetScaleSpeedY(0)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    sprite('null', 10)
    SetScaleSpeedY(85)
    sprite('null', 20)
    ConstantAlphaModifier(-13)
    SetScaleXPerFrame(10)
    SetScaleSpeedZ(10)
    loopRest()


@State
def mi440_jusoFireBG():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        LinkParticle('mief440_blm')
        Eff3DEffect('mieff440_bg00', '')
        Size(1000)
        AlphaValue(0)
        uponSendToLabel(32, 1)
    sprite('null', 30)
    ConstantAlphaModifier(8)
    label(0)
    sprite('null', 20)
    SetScaleSpeedY(0)
    gotoLabel(0)
    label(1)
    sprite('null', 30)
    SetScaleX(1500)
    sprite('null', 20)
    ConstantAlphaModifier(-13)
    loopRest()


@State
def mi440_GaikotuEx():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        ObjectHitbox(2)
        Eff3DEffect('mieff440_gaikotu00', '')
        Size(1000)
        AddScaleY(200)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)
        TeleportToObject(22)
    sprite('null', 25)
    SetScaleSpeed(40)
    CreateObject('mi440_GaikotuAura', -1)
    CommonSE('019_quake_1')
    label(0)
    sprite('null', 2)
    SetScaleSpeed(0)
    AddY(7000)
    AddX(-3500)
    CommonSE('021_bonecleak_1')
    sprite('null', 2)
    AddY(-7000)
    AddX(3500)
    CommonSE('012_stab_fast')
    gotoLabel(0)
    label(1)
    sprite('null', 32767)
    TriggerUponForState('mi440_GaikotuAura', 32)
    Eff3DEffect('mieff440_gaikotu01', '')
    loopRest()
    label(2)
    sprite('null', 32767)
    PaletteIndex(1)
    ColorFromPaletteIndex(194)
    loopRest()


@State
def mi440_Gaikotu():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        ObjectHitbox(2)
        Eff3DEffect('mieff440_gaikotu00', '')
        Size(1000)
        AddScaleY(200)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
        TeleportToObject(22)
    sprite('null', 25)
    SetScaleSpeed(40)
    CreateObject('mi440_GaikotuAura', -1)
    CommonSE('019_quake_1')
    label(0)
    sprite('null', 2)
    SetScaleSpeed(0)
    AddY(7000)
    AddX(-3500)
    CommonSE('021_bonecleak_1')
    sprite('null', 2)
    AddY(-7000)
    AddX(3500)
    CommonSE('012_stab_fast')
    gotoLabel(0)
    label(1)
    sprite('null', 32767)
    TriggerUponForState('mi440_GaikotuAura', 32)
    Eff3DEffect('mieff440_gaikotu01', '')
    loopRest()


@State
def mi440_GaikotuAura():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Size(1100)
        LinkParticle('mief440_ground')
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 1)
    PrivateSE('mise_15')
    PrivateSE('mise_15')
    PrivateSE('mise_14')


@State
def mi440_GaikotuSotoba():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        ObjectHitbox(2)
        Eff3DEffect('mieff440_sotoba', '')
        Size(1800)
        AddScaleY(200)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)
        TeleportToObject(22)
    label(0)
    sprite('null', 2)
    SetScaleSpeed(0)
    AddY(-7000)
    AddX(3500)
    sprite('null', 2)
    AddY(7000)
    AddX(-3500)
    gotoLabel(0)
    label(1)
    sprite('null', 32767)
    Eff3DEffect('mieff440_sotoba2', '')
    loopRest()
    label(2)
    sprite('null', 32767)
    PaletteIndex(1)
    ColorFromPaletteIndex(194)
    loopRest()


@State
def mi440_BlackBG():

    def upon_IMMEDIATE():
        BlendMode_Sub()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('mieff440_bg01', '')
        uponSendToLabel(32, 1)
    sprite('null', 32767)
    label(1)
    sprite('null', 26)
    ConstantAlphaModifier(-26)
    loopRest()


@State
def mi440_Flash():

    def upon_IMMEDIATE():
        RenderLayer(4)
        BlendMode_Add()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('mieff440_bg01', '')
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
    sprite('null', 2)
    sprite('null', 5)
    ConstantAlphaModifier(-51)
    loopRest()


@State
def mi440_Blood():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        BlendMode_Add()
        AlphaValue(255)
        IgnoreScreenfreeze(1)

        def upon_16():
            PrivateFunction3(22, -1250, 35000, 100, 1)
        Size(800)
        RenderLayer(1)
    sprite('mief406_10', 3)
    sprite('mief406_11', 3)
    sprite('mief406_12', 3)
    sprite('mief406_13', 3)
    sprite('mief406_14', 3)
    sprite('mief406_15', 3)
    ConstantAlphaModifier(-26)
    sprite('mief406_16', 3)
    sprite('mief406_17', 3)


@State
def mi440_BloodBig():

    def upon_IMMEDIATE():

        def upon_16():
            PrivateFunction3(22, 0, 50000, 100, 1)
        E0EAEffectPosition(22)
        PaletteIndex(1)
        BlendMode_Add()
        AlphaValue(255)
        LinkParticle('mief440_blood')
        IgnoreScreenfreeze(1)
        AddY(300000)
        Size(1200)
        RenderLayer(1)
        Flip()
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 4)
    ScreenShake(10000, 10000)
    CreateParticle('mief440_blood_tb', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 20)
    SetScaleSpeed(-30)
    sprite('null', 10)
    ConstantAlphaModifier(-51)
    loopRest()


@State
def mi440_BloodBigEX():

    def upon_IMMEDIATE():

        def upon_16():
            PrivateFunction3(22, -1250, 80000, 100, 1)
        E0EAEffectPosition(22)
        PaletteIndex(1)
        BlendMode_Add()
        AlphaValue(255)
        LinkParticle('mief440_bloodEX')
        IgnoreScreenfreeze(1)
        AddY(300000)
        Size(2000)
        RenderLayer(1)
        Flip()
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 4)
    ScreenShake(10000, 10000)
    CreateParticle('mief440_blood_tbEX', -1)
    ParticleSize(800)
    CallCustomizableParticle('mief440_bloodex', -1)
    sprite('null', 4)
    ScreenShake(10000, 10000)
    gotoLabel(0)
    label(1)
    sprite('null', 20)
    SetScaleSpeed(-60)
    sprite('null', 10)
    ConstantAlphaModifier(-51)
    loopRest()


@State
def mi440_Camera():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreFinishStop(1)
        IgnoreScreenfreeze(1)
        RemoveOnCallStateEnd(2)
        uponSendToLabel(32, 1)
        uponSendToLabel(33, 2)
    label(0)
    sprite('null', 32767)
    TeleportToObject(22)
    CameraControlEnable(1)
    CameraNoCeiling(1)
    CameraNoScreenCollision(1)
    CameraControlInfinity(1)
    label(1)
    sprite('null', 32767)
    label(2)
    sprite('null', 1)
    CameraControlInfinity(0)


@State
def mi440_Juwa():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(194)
        Eff3DEffect('mieff440_juwa00', '')
        RemoveOnCallStateEnd(2)
        AddY(300000)
        SetScaleX(850)
        SetScaleY(900)
        uponSendToLabel(32, 0)
    sprite('null', 55)
    sprite('null', 32767)
    Eff3DEffect('mieff440_bg01', '')
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    loopRest()


@State
def mi450_Start():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Normal()
        Eff3DEffect('mieff450_atkstart', '')
        IgnoreScreenfreeze(1)
        SetScaleX(600)
        SetScaleY(600)
        SetScaleZ(100)
        AlphaValue(200)
        ContinueState(300)

        def upon_PLAYER_DAMAGED():
            DeleteObject(23)
    sprite('null', 10)
    CreateParticle('mief450_atkfirst00_blm', -1)
    CreateObject('mi450_StartSub', -1)
    label(0)
    sprite('null', 10)
    CreateObject('mi450_StartSub', -1)
    loopRest()
    gotoLabel(0)


@State
def mi450_StartSub():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        BlendMode_Normal()
        Eff3DEffect('mieff400_createaura', '')
        AlphaValue(0)
        SetScaleY(1000)
        SetScaleX(1500)
        SetScaleZ(1500)
        PaletteIndex(1)
        ColorFromPaletteIndex(84)
        IgnoreScreenfreeze(1)

        def upon_PLAYER_DAMAGED():
            DeleteObject(23)
    sprite('null', 10)
    ConstantAlphaModifier(26)
    sprite('null', 10)
    ConstantAlphaModifier(0)
    sprite('null', 10)
    ConstantAlphaModifier(0)
    SetScaleXPerFrame(-8)
    SetScaleSpeedZ(-8)
    ConstantAlphaModifier(-26)


@State
def AstralCamera():

    def upon_IMMEDIATE():
        HUDVisibillity(1)
        CameraControlEnable(1)
        CameraNoCeiling(1)
        CameraNoScreenCollision(1)
        uponSendToLabel(32, 0)
        uponSendToLabel(33, 1)
        uponSendToLabel(34, 2)
        uponSendToLabel(35, 3)
        uponSendToLabel(36, 5)
        uponSendToLabel(37, 6)
    sprite('null', 32767)
    CameraPosition(1500)
    E0EAEffectPosition(3)
    label(0)
    sprite('null', 10)
    E0EAEffectPosition(0)
    CreateObject('mi450_Kirikae2', -1)
    CreateObject('mi450_OnryoBasiraCamera', -1)
    sprite('null', 32767)
    CreateObject('mi450_OnryoBasiraCamera', -1)

    def RunOnObject_1():
        AddY(-180000)
        AddScale(100)
    TeleportToObject(22)
    physicsYImpulse(24200)
    CameraPosition(1000)
    label(1)
    sprite('null', 32767)
    TriggerUponForState('mi450_OnryoBasiraCamera', 32)
    EndMomentum(1)
    CameraPosition(1600)
    label(2)
    sprite('null', 1)
    CameraPosition(1000)
    CameraFast(1)
    sprite('null', 1)
    CameraPosition(1100)
    sprite('null', 1)
    CameraPosition(1200)
    sprite('null', 1)
    CameraPosition(1300)
    sprite('null', 1)
    CameraPosition(1400)
    sprite('null', 1)
    CameraPosition(1500)
    sprite('null', 1)
    CameraPosition(1600)
    sprite('null', 32767)
    EndMomentum(1)
    label(3)
    sprite('null', 4)
    E0EAEffectPosition(22)
    physicsYImpulse(-1500)
    label(4)
    sprite('null', 4)
    ScreenShake(10000, 10000)
    gotoLabel(4)
    label(5)
    sprite('null', 32767)
    ScreenShake(200000, 200000)
    E0EAEffectPosition(2)
    physicsYImpulse(0)
    AddY(-250000)
    label(6)
    sprite('null', 60)
    sprite('null', 32767)
    CameraPosition(1100)


@State
def mi450_OnryoBasiraCamera():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(84)
        E0EAEffectPosition(2)
        Eff3DEffect('mieff450_onryo_hasira00', '')
        LinkParticle('mief450_onryo_tornado')
        RemoveOnCallStateEnd(2)
        Size(1200)
        AlphaValue(0)
        RandAddScaleX(-400, 0)
        AddY(-400000)
        uponSendToLabel(32, 1)
    sprite('null', 30)
    CreateObject('mi450_OnryoBasiraBG2', -1)
    ConstantAlphaModifier(7)
    label(0)
    sprite('null', 12)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    CreateObject('mi450_OnryoBasiraSub3', -1)
    ScreenShake(10000, 10000)
    ConstantAlphaModifier(-26)
    SetScaleSpeedY(-30)
    SetScaleXPerFrame(60)
    SetScaleSpeedZ(60)
    sprite('null', 20)
    CreateObject('mi450_OnryoBasiraEnd', -1)


@State
def mi450_OnryoBasiraSub3():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff450_onryo_hasira02', '')
        LinkParticle('mief450_onryo_tornado')
        Flip()
        AlphaValue(0)
        AddY(-250000)
        SetScaleY(2000)
        SetScaleX(4000)
        SetScaleZ(4000)
        PaletteIndex(1)
        ColorFromPaletteIndex(84)
    sprite('null', 5)
    ConstantAlphaModifier(26)
    sprite('null', 20)
    sprite('null', 10)
    ConstantAlphaModifier(-26)
    SetScaleSpeedZ(25)
    SetScaleXPerFrame(25)


@State
def mi450_OnryoBasiraCameraSub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff404_aura00', '')
        RemoveOnCallStateEnd(2)
        AlphaValue(0)
        SetScaleY(1400)
        SetScaleX(1100)
        SetScaleZ(1100)
        Flip()
    sprite('null', 5)
    ConstantAlphaModifier(20)
    sprite('null', 20)
    ConstantAlphaModifier(0)
    SetScaleXPerFrame(-2)
    SetScaleSpeedZ(-2)
    physicsYImpulse(8000)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mi450_OnryoBasiraEnd():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(84)
        Eff3DEffect('mieff450_onryo_housha00', '')
        AddScale(1200)
        AddY(300000)
        RenderLayer(5)
    sprite('null', 30)
    AlphaValue(100)
    SetScaleSpeed(45)
    sprite('null', 20)
    ConstantAlphaModifier(-13)


@State
def mi450_OnryoBasira():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(84)
        Size(1500)
        AlphaValue(0)
        AddY(-400000)
        uponSendToLabel(32, 1)
        RemoveOnCallStateEnd(2)
        Eff3DEffect('mieff450_onryo_hasira01', '')
        SetScaleX(1500)
        SetScaleZ(1500)
    sprite('null', 12)
    ConstantAlphaModifier(51)
    CreateObject('mi450_OnryoStart', -1)

    def RunOnObject_1():
        AddScale(1400)
    sprite('null', 6)
    CreateObject('mi450_OnryoBasiraSub', -1)
    CreateObject('mi450_OnryoStart', -1)

    def RunOnObject_1():
        AddScale(1250)
    ScreenShake(10000, 10000)
    sprite('null', 6)
    ScreenShake(10000, 10000)
    sprite('null', 6)
    CreateObject('mi450_OnryoBasiraSub2', -1)
    ScreenShake(10000, 10000)
    sprite('null', 6)
    ScreenShake(10000, 10000)
    label(0)
    sprite('null', 6)
    CreateObject('mi450_OnryoBasiraSub', -1)
    CreateObject('mi450_OnryoStart', -1)

    def RunOnObject_1():
        AddScale(1250)
    ScreenShake(10000, 10000)
    sprite('null', 6)
    ScreenShake(10000, 10000)
    sprite('null', 6)
    CreateObject('mi450_OnryoBasiraSub2', -1)
    ScreenShake(10000, 10000)
    sprite('null', 6)
    ScreenShake(10000, 10000)
    gotoLabel(0)
    label(1)
    sprite('null', 1)


@State
def mi450_OnryoBasiraBG2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(84)
        Eff3DEffect('mieff450_onryo_hasira00b', '')
        RemoveOnCallStateEnd(2)
        SetPosXByScreenPer(50)
        SetPosYByScreenPer(50)
        AlphaValue(0)
        ConstantAlphaModifier(10)
        physicsYImpulse(10500)
    sprite('null', 32767)


@State
def mi450_OnryoBasiraSub():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        PaletteIndex(1)
        ColorFromPaletteIndex(84)
        LinkParticle('mief450_onryo_tornado')
        Eff3DEffect('mieff450_onryo_hasira00', '')
        RemoveOnCallStateEnd(2)
        Size(1500)
        AlphaValue(0)
        RandAddScaleX(-400, 0)
    sprite('null', 30)
    ConstantAlphaModifier(10)
    physicsYImpulse(10500)
    sprite('null', 120)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mi450_OnryoBasiraSub2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('mief450_onryo_tornado')
        Eff3DEffect('mieff450_onryo_hasira00', '')
        RemoveOnCallStateEnd(2)
        SetScaleX(1300)
        SetScaleY(1400)
        SetScaleZ(1300)
        AlphaValue(0)
    sprite('null', 30)
    ConstantAlphaModifier(10)
    physicsYImpulse(10500)
    sprite('null', 120)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mi450_OnryoStart():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff404_aura00', '')
        RemoveOnCallStateEnd(2)
        AlphaValue(0)
        SetScaleY(1400)
        SetScaleX(1100)
        SetScaleZ(1100)
        Flip()
    sprite('null', 5)
    ConstantAlphaModifier(51)
    sprite('null', 20)
    SetScaleXPerFrame(-2)
    SetScaleSpeedZ(-2)
    physicsYImpulse(8000)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mi450_Kirikae():

    def upon_IMMEDIATE():
        RenderLayer(1)
        BlendMode_Normal()
        Size(2500)
        Eff3DEffect('mieff450_onryo_Scroll', '')
        E0EAEffectPosition(2)
    sprite('null', 99)


@State
def mi450_Kirikae2():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        RenderLayer(1)
        BlendMode_Normal()
        Size(2000)
        AddY(-1000000)
        AddX(-400000)
        Eff3DEffect('mieff450_onryo_Scroll2', '')
        E0EAEffectPosition(2)
    sprite('null', 39)


@State
def mi450_CutTest():

    def upon_IMMEDIATE():
        E0EAEffectPosition(2)
        BlendMode_Normal()
        uponSendToLabel(32, 0)
        Size(1600)
        AddY(340000)
        AddX(-50000)
        PaletteIndex(0)
        FaceLeft()
        LinkParticle('mief450_eyebloom')
    sprite('mi450cutin_00', 5)
    SetScaleSpeed(100)
    ScreenShake(10000, 10000)
    CreateParticle('mief450_feed', -1)
    CreateObject('mi450_CutTestGrow', -1)
    sprite('mi450cutin_00', 60)
    SetScaleSpeed(1)
    sprite('mi450cutin_00', 20)
    CreateObject('mi450_CutTest2', -1)
    sprite('mi450cutin_00', 32767)
    label(0)
    sprite('null', 10)
    TriggerUponForState('mi450_CutTestGrow', 32)
    TriggerUponForState('mi450_CutTest2', 32)
    SetScaleSpeed(100)
    ConstantAlphaModifier(-26)


@State
def mi450_CutTest2():

    def upon_IMMEDIATE():
        BlendMode_Sub()
        RenderLayer(1)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        uponSendToLabel(32, 0)
        PaletteIndex(3)
    sprite('mi450cutin_mask00', 20)
    CreateObject('mi450_CutInBG', -1)
    AlphaValue(0)
    ConstantAlphaModifier(10)
    CommonSE('012_stab_deep')
    CommonSE('012_stab_deep')
    PrivateSE('mise_09')
    sprite('mi450cutin_mask00', 32767)
    ConstantAlphaModifier(0)
    label(0)
    sprite('mi450cutin_mask00', 10)
    ConstantAlphaModifier(-13)
    DespawnEAEffect('mi450_CutInBG')


@State
def mi450_CutTestGrow():

    def upon_IMMEDIATE():
        BlendMode_Sub()
        RenderLayer(1)
        E0EAEffectPosition(2)
        E0EAEffectScale(2)
        E0EAEffectScale(2)
        RemoveOnCallStateEnd(2)
        PaletteIndex(3)
        uponSendToLabel(32, 0)
    sprite('mi450cutin_mask01', 20)
    AlphaValue(0)
    ConstantAlphaModifier(3)
    sprite('mi450cutin_mask01', 32767)
    ConstantAlphaModifier(0)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mi450_CutInBG():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff450_juwa', '')
        E0EAEffectPosition(2)
        Size(1300)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(26)
    label(0)
    sprite('null', 2)
    AddScaleX(2)
    AddScaleY(-2)
    sprite('null', 2)
    AddScaleX(-2)
    AddScaleY(2)
    gotoLabel(0)


@State
def mi450_BigOnryo():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('mief450_Bigonryoaura')
        Eff3DEffect('mieff450_gaikotu1_start00', '')
        Size(2750)
        AddY(900000)
        uponSendToLabel(32, 0)
    sprite('null', 1)
    AlphaValue(0)
    PrivateSE('mise_07')
    sprite('null', 109)
    AlphaValue(255)
    sprite('null', 32767)
    E0EAEffectPosition(2)
    label(0)
    sprite('null', 10)
    physicsYImpulse(-80000)


@State
def mi450_BigOnryo2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('mief450_Bigonryoaura')
        Eff3DEffect('mieff450_gaikotu2_start00', '')
        Size(3000)
        AddY(600000)
        uponSendToLabel(32, 0)
    sprite('null', 1)
    AlphaValue(0)
    sprite('null', 118)
    AlphaValue(255)
    sprite('null', 15)
    E0EAEffectPosition(2)
    physicsXImpulse(10000)
    sprite('null', 32767)
    physicsXImpulse(0)
    label(0)
    sprite('null', 40)
    AddX(75000)
    physicsXImpulse(15000)
    physicsYImpulse(-120000)
    Rotation(-15000)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mi450_BigOnryo3():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('mief450_Bigonryoaura')
        Eff3DEffect('mieff450_gaikotu3_start00', '')
        Size(3000)
        AddY(80000)
        uponSendToLabel(32, 0)
    sprite('null', 1)
    AlphaValue(0)
    sprite('null', 138)
    AlphaValue(255)
    sprite('null', 32767)
    E0EAEffectPosition(2)
    label(0)
    sprite('null', 15)
    physicsYImpulse(-70000)


@State
def mi450_GamenAura00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff450_gamenAura', '')
        AddY(400000)
        Size(1400)
        AddScaleZ(300)
    sprite('null', 32767)


@State
def mi450_GroundAura():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        E0EAEffectPosition(2)
        LinkParticle('mief450_groundshock')
        Eff3DEffect('mieff450_groundshock00', '')
        Size(1500)
        AddScaleY(300)
        AbsoluteY(0)
        uponSendToLabel(32, 1)
    label(0)
    sprite('null', 5)
    CreateObject('mi450_GroundAuraCircle', -1)
    ScreenShake(15000, 15000)
    AddScale(80)
    CommonSE('019_quake_1')
    sprite('null', 5)
    ScreenShake(15000, 15000)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    ConstantAlphaModifier(-13)
    SetScaleSpeed(30)
    ScreenShake(25000, 25000)
    sprite('null', 10)
    ScreenShake(25000, 25000)
    CreateParticle('mief450_spark', -1)


@State
def mi450_GroundAuraCircle():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff450_groundshock01', '')
        Size(1000)
        AddY(80000)
    sprite('null', 5)
    SetScaleSpeed(200)
    physicsYImpulse(10000)
    sprite('null', 10)
    ConstantAlphaModifier(-26)


@State
def mi450_fallspeed():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AlphaValue(100)
        E0EAEffectPosition(2)
        Eff3DEffect('mieff450_fallspeed', '')
        LinkParticle('mief450_speed')
        AddY(650000)
        SetScaleX(2000)
        SetScaleY(2000)
    sprite('null', 32767)


@State
def mi450_EndAura():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        AlphaValue(180)
        LinkParticle('mief450_endaura')
        Eff3DEffect('mieff_cmnaura00', '')
        Size(3000)
    sprite('null', 75)
    SetScaleSpeed(-5)
    sprite('null', 10)
    CreateParticle('mief450_endaura2', -1)
    sprite('null', 40)
    ConstantAlphaModifier(-4)
    SetScaleSpeedY(-40)
    SetScaleXPerFrame(40)


@State
def mi450_EndAnim():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff450_endeff00', '')
        Size(2100)
        RenderLayer(1)
        AddY(400000)
    sprite('null', 24)


@State
def mi600_Cicle():

    def upon_IMMEDIATE():
        RenderLayer(2)
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddY(200000)
    sprite('null', 10)
    CreateObject('mi600_CicleA', -1)
    sprite('mief600_00', 4)
    sprite('mief600_01', 4)
    sprite('mief600_02', 4)
    sprite('mief600_03', 4)
    CreateParticle('mief600_moya', 0)
    CreateParticle('mief600_moya', 1)
    CreateParticle('mief600_moya', 2)
    CreateParticle('mief600_moya', 3)
    CreateParticle('mief600_moya', 4)
    CreateParticle('mief600_moya', 5)
    sprite('mief600_03', 100)
    CreateObject('mi600_Ray', -1)
    Visibility(1)
    CreateObject('mi600_CicleAdd', 6)


@State
def mi600_CicleA():

    def upon_IMMEDIATE():
        RenderLayer(2)
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddY(150000)
        AddX(-50000)
    sprite('mief600_00a', 10)
    SetScaleSpeed(60)


@State
def mi600_CicleAdd():

    def upon_IMMEDIATE():
        RenderLayer(2)
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AlphaValue(255)
        Size(2000)
    sprite('null', 80)
    ParticleLayer(2)
    CallPrivateEffect('mief600_ray')
    sprite('null', 15)
    ConstantAlphaModifier(-17)


@State
def mi600_Ray():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        RenderLayer(5)
        Eff3DEffect('mieff600_ray', '')
        ObjectHitbox(2)
        ScreenCollision(1)
        CameraNoScreenCollision(1)
        AddY(160000)
        AddX(-50000)
        SetScaleX(800)
        SetScaleY(900)
    sprite('null', 80)
    AlphaValue(0)
    ConstantAlphaModifier(26)
    sprite('null', 20)
    ConstantAlphaModifier(-13)


@State
def mi600_Huku():

    def upon_IMMEDIATE():
        PaletteIndex(6)
        E0EAEffectPosition(2)
        RemoveOnCallStateEnd(2)
    sprite('mi600_02y', 8)
    CreateObject('mi600_HukuGround', 0)
    sprite('mi600_03y', 8)
    sprite('mi600_04y', 8)
    sprite('mi600_05y', 8)
    E0EAEffectPosition(0)
    sprite('mi600_06y', 8)
    sprite('mi600_07y', 8)
    sprite('mi600_07y', 5)
    ConstantAlphaModifier(-51)


@State
def mi600_HukuGround():

    def upon_IMMEDIATE():
        LinkParticle('mief600_groundsub')
    sprite('null', 50)
    PrivateSE('mise_12')
    label(0)
    sprite('null', 30)
    ConstantAlphaModifier(-8)
    loopRest()


@State
def mi601_doro():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        AddY(12500)
        Size(1150)
    sprite('mief601_00', 8)
    CreateParticle('mief601_moya', 0)
    CreateObject('mi601_Smoke', -1)
    sprite('mief601_01', 8)
    CreateParticle('mief601_moya', 0)
    CreateParticle('mief601_moya', 1)
    CreateParticle('mief601_moya', 2)
    sprite('mief601_02', 7)
    CreateParticle('mief601_moya', 0)
    CreateParticle('mief601_moya', 1)
    CreateParticle('mief601_moya', 2)
    CreateParticle('mief601_moya', 3)
    CreateParticle('mief601_moya', 4)
    sprite('mief601_03', 6)
    CreateParticle('mief601_moya', 0)
    CreateParticle('mief601_moya', 1)
    CreateParticle('mief601_moya', 2)
    CreateParticle('mief601_moya', 3)
    CreateParticle('mief601_moya', 4)
    CreateObject('mi601_doro3D', -1)
    sprite('mief601_04', 4)
    ScreenShake(2000, 2000)
    CreateObject('mi601_Smoke', -1)
    CreateParticle('mief601_siru', 0)
    CreateParticle('mief601_siru', 1)
    CreateParticle('mief601_siru', 2)
    CreateParticle('mief601_siru', 3)
    CreateParticle('mief601_siru', 4)
    CreateParticle('mief601_siru', 5)
    sprite('mief601_05', 4)
    CreateParticle('mief601_siru', 0)
    CreateParticle('mief601_siru', 1)
    CreateParticle('mief601_siru', 2)
    CreateParticle('mief601_siru', 3)
    CreateParticle('mief601_siru', 4)
    sprite('mief601_06', 4)
    sprite('mief601_07', 4)
    sprite('mief601_08', 4)
    sprite('mief601_09', 10)
    BlendMode_Normal()
    ConstantAlphaModifier(-26)


@State
def mi601_Smoke():

    def upon_IMMEDIATE():
        AlphaValue(0)
        BlendMode_Normal()
        Eff3DEffect('mieff601_smoke00', '')
        Size(800)
    sprite('null', 10)
    ConstantAlphaModifier(4)
    sprite('null', 10)
    ConstantAlphaModifier(0)
    sprite('null', 10)
    ConstantAlphaModifier(-6)
    SetScaleSpeedY(-10)
    SetScaleXPerFrame(55)
    SetScaleSpeedZ(55)


@State
def mi601_doro3D():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('mieff601_doro', '')
        Size(900)
    sprite('null', 6)
    AlphaValue(0)
    sprite('null', 18)
    AlphaValue(255)
    sprite('null', 5)
    ConstantAlphaModifier(-51)


@State
def mi611_Camera():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        ObjectHitbox(2)
        ScreenCollision(1)
        CameraNoScreenCollision(1)
        CameraControlEnable(1)
        AddY(300000)
    sprite('null', 32767)
    SetBackground(2)


@State
def mi611_RayColor():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('mieff611_ray01', '')
        ObjectHitbox(2)
        ScreenCollision(1)
        CameraNoScreenCollision(1)
        Size(1470)
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(26)
    sprite('null', 32767)
    ConstantAlphaModifier(0)


@State
def mi611_Ray():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('mieff611_ray00', '')
        ObjectHitbox(2)
        ScreenCollision(1)
        CameraNoScreenCollision(1)
        AddY(280000)
        AddX(-5000)
        Size(1600)
        AddRotationPerFrame(30)
        PaletteIndex(0)
        ColorFromPaletteIndex(64)
        ParticleColorFromPalette(64, 64, 64)
        CallPrivateEffect('mief611_ray')
    sprite('null', 10)
    AlphaValue(0)
    ConstantAlphaModifier(26)
    CreateObject('mi611_RayColor', -1)
    sprite('null', 32767)
    ConstantAlphaModifier(0)


@State
def mi611_Soul():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        ObjectHitbox(2)
        ScreenCollision(1)
        CameraNoScreenCollision(1)
    sprite('null', 36)
    LinkParticle('mief600_soul2')
    Size(1200)
    sprite('null', 32767)
    CreateObject('mi611_SoulCore', -1)


@State
def mi611_SoulCore():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        RemoveOnCallStateEnd(2)
        ObjectHitbox(2)
        ScreenCollision(1)
        CameraNoScreenCollision(1)
    sprite('null', 32767)
    LinkParticle('mief600_soul')
    CreateObject('mi611_SoulCoreYugami', -1)


@State
def mi611_SoulCoreYugami():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        IgnoreScreenfreeze(1)
        IgnoreFinishStop(1)
        Size(400)
        AddRotationPerFrame(5000)
        PlayerTransparency(15000)
        ParticleTransparency(1)
    label(0)
    sprite('vrmi408_yugami', 15)
    gotoLabel(0)


@State
def mi610_Kaiho():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        E0EAEffectPosition(2)
        AddY(200000)
        Size(250)
    sprite('vrmi432_yugami', 7)
    ParticleTransparency(1)
    PlayerTransparency(250000)
    Unknown3059(-12000)
    SetScaleSpeed(100)
    sprite('vrmi432_yugami', 8)
    SetScaleSpeed(50)


@State
def mi900_Fire():

    def upon_IMMEDIATE():
        BlendMode_Add()
        RemoveOnCallStateEnd(2)
        Eff3DEffect('mieff440_jusoFire00', '')
        Size(160)
        AlphaValue(0)
        uponSendToLabel(32, 1)
    sprite('null', 15)
    sprite('null', 60)
    ConstantAlphaModifier(4)
    label(0)
    sprite('null', 2)
    gotoLabel(0)


@State
def mi900_Gaikotu():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        CreateObject('mi900_HinoTama', -1)
        BlendMode_Normal()
        AlphaValue(0)
        AddY(-5000)
        LinkParticle('mief900_blm')
    sprite('mief900_00', 60)
    ConstantAlphaModifier(3)
    label(0)
    sprite('mief900_00', 3)
    ConstantAlphaModifier(0)
    sprite('mief900_01', 3)
    sprite('mief900_02', 3)
    sprite('mief900_03', 6)
    sprite('mief900_04', 3)
    sprite('mief900_05', 3)
    sprite('mief900_03', 3)
    gotoLabel(0)


@State
def mi900_Gaikotu2():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        CreateObject('mi900_HinoTama2', -1)
        BlendMode_Normal()
        AlphaValue(0)
        LinkParticle('mief900_blm')
    sprite('mief900_00', 60)
    ConstantAlphaModifier(3)
    label(0)
    sprite('mief900_04', 4)
    ConstantAlphaModifier(0)
    sprite('mief900_05', 4)
    sprite('mief900_03', 6)
    sprite('mief900_00', 4)
    sprite('mief900_01', 4)
    sprite('mief900_02', 4)
    sprite('mief900_03', 4)
    gotoLabel(0)


@State
def mi900_Gaikotu3():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        CreateObject('mi900_HinoTama3', -1)
        BlendMode_Normal()
        AlphaValue(0)
        LinkParticle('mief900_blm')
    sprite('mief900_00', 60)
    ConstantAlphaModifier(3)
    label(0)
    sprite('mief900_02', 4)
    ConstantAlphaModifier(0)
    sprite('mief900_03', 4)
    sprite('mief900_04', 4)
    sprite('mief900_05', 4)
    sprite('mief900_03', 6)
    sprite('mief900_00', 4)
    sprite('mief900_01', 4)
    gotoLabel(0)


@State
def mi900_HinoTama():

    def upon_IMMEDIATE():
        PaletteIndex(3)
        RemoveOnCallStateEnd(2)
        RenderLayer(11)
        BlendMode_Add()
        AddX(5500)
    label(0)
    sprite('mief900_10', 5)
    sprite('mief900_11', 5)
    sprite('mief900_12', 5)
    sprite('mief900_13', 5)
    sprite('mief900_14', 5)
    sprite('mief900_15', 5)
    sprite('mief900_17', 5)
    sprite('mief900_18', 5)
    gotoLabel(0)


@State
def mi900_HinoTama2():

    def upon_IMMEDIATE():
        PaletteIndex(3)
        RemoveOnCallStateEnd(2)
        RenderLayer(11)
        BlendMode_Add()
        AddX(5500)
    label(0)
    sprite('mief900_13', 5)
    sprite('mief900_14', 5)
    sprite('mief900_15', 5)
    sprite('mief900_17', 5)
    sprite('mief900_18', 5)
    sprite('mief900_10', 5)
    sprite('mief900_11', 5)
    sprite('mief900_12', 5)
    gotoLabel(0)


@State
def mi900_HinoTama3():

    def upon_IMMEDIATE():
        PaletteIndex(3)
        RemoveOnCallStateEnd(2)
        RenderLayer(11)
        BlendMode_Add()
        AddX(5500)
        Flip()
    label(0)
    sprite('mief900_17', 5)
    sprite('mief900_18', 5)
    sprite('mief900_10', 5)
    sprite('mief900_11', 5)
    sprite('mief900_12', 5)
    sprite('mief900_13', 5)
    sprite('mief900_14', 5)
    sprite('mief900_15', 5)
    gotoLabel(0)


@State
def mi900_bloom():

    def upon_IMMEDIATE():
        RemoveOnCallStateEnd(2)
        PaletteIndex(0)
        ColorFromPaletteIndex(64)
        BlendMode_Add()
        Unknown23180(1)
    sprite('vr_mief900_90', 32767)


@State
def Act3Event_EffWarpOut():

    def upon_IMMEDIATE():
        PaletteIndex(1)
        RemoveOnCallStateEnd(2)
        AddX(-52000)
        AddY(12500)
        Size(1150)
    sprite('mief601_00', 8)
    CreateParticle('mief601_moya', 0)
    CreateObject('mi601_Smoke', -1)
    sprite('mief601_01', 8)
    CreateParticle('mief601_moya', 0)
    CreateParticle('mief601_moya', 1)
    CreateParticle('mief601_moya', 2)
    sprite('mief601_02', 7)
    CreateParticle('mief601_moya', 0)
    CreateParticle('mief601_moya', 1)
    CreateParticle('mief601_moya', 2)
    CreateParticle('mief601_moya', 3)
    CreateParticle('mief601_moya', 4)
    sprite('mief601_03', 21)
    CreateParticle('mief601_moya', 0)
    CreateParticle('mief601_moya', 1)
    CreateParticle('mief601_moya', 2)
    CreateParticle('mief601_moya', 3)
    CreateParticle('mief601_moya', 4)
    CreateObject('mi601_doro3D', -1)
    sprite('mief601_02', 7)
    CreateParticle('mief601_moya', 0)
    CreateParticle('mief601_moya', 1)
    CreateParticle('mief601_moya', 2)
    CreateParticle('mief601_moya', 3)
    CreateParticle('mief601_moya', 4)
    sprite('mief601_01', 7)
    CreateParticle('mief601_siru', 0)
    CreateParticle('mief601_siru', 1)
    CreateParticle('mief601_siru', 2)
    CreateParticle('mief601_siru', 3)
    CreateParticle('mief601_siru', 4)
    sprite('mief601_00', 7)
    BlendMode_Normal()
    ConstantAlphaModifier(-26)
